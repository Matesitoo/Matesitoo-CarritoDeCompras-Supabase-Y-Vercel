from http.server import BaseHTTPRequestHandler
import json
import sys
import os

#Configurar path para importar los modulos
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

try:
    #Importar los modulos existentes
    from managers import productosManager, clientesManager, pedidosManager
    from routes import clientRouter, productoRouter, pedidoRouter
    has_modules = True
except ImportError as e:
    print(f"No se pudieron importar modulos: {e}")
    has_modules = False

class Handler(BaseHTTPRequestHandler):
    
    def _set_cors_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    
    def do_OPTIONS(self):
        self.send_response(200)
        self._set_cors_headers()
        self.end_headers()
    
    def _send_json_response(self, status_code, data):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self._set_cors_headers()
        self.end_headers()
        self.wfile.write(json.dumps(data, ensure_ascii=False).encode('utf-8'))
    
    def do_GET(self):
        try:
            print(f"GET recibido: {self.path}")
            
            # Rutas principales
            if self.path == '/':
                response = {
                    "message": "API Matesitoo Carrito de Compras funcionando",
                    "status": "success",
                    "endpoints": {
                        "clientes": "/clientes",
                        "productos": "/productos", 
                        "pedidos": "/pedidos",
                        "health": "/health"
                    }
                }
                self._send_json_response(200, response)
            
            elif self.path == '/health':
                response = {
                    "status": "healthy",
                    "service": "Matesitoo API",
                    "timestamp": "2024-01-01T00:00:00Z"
                }
                self._send_json_response(200, response)
            
            elif self.path == '/productos':
                if has_modules:
                    #Aca integramos con productsManager
                    response = {
                        "message": "Endpoint productos - Implementar con productsManager",
                        "action": "get_productos"
                    }
                else:
                    response = {
                        "message": "Módulo productsManager no disponible",
                        "productos": [
                            {"id": 1, "nombre": "Mate ejemplo", "precio": 100},
                            {"id": 2, "nombre": "Bombilla ejemplo", "precio": 50}
                        ]
                    }
                self._send_json_response(200, response)
            
            elif self.path == '/clientes':
                response = {
                    "message": "Endpoint clientes - Implementar con clientesManager",
                    "action": "get_clientes"
                }
                self._send_json_response(200, response)
                
            else:
                response = {
                    "error": "Ruta no encontrada",
                    "path": self.path,
                    "available_routes": ["/", "/health", "/productos", "/clientes", "/pedidos"]
                }
                self._send_json_response(404, response)
                
        except Exception as e:
            print(f"Error en GET: {e}")
            response = {
                "error": "Error interno del servidor",
                "details": str(e)
            }
            self._send_json_response(500, response)
    
    def do_POST(self):
        try:
            print(f"POST recibido: {self.path}")
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length) if content_length > 0 else b'{}'
            
            data = json.loads(post_data.decode('utf-8')) if post_data else {}
            
            response = {
                "message": "POST procesado correctamente",
                "path": self.path,
                "data_received": data,
                "action": "Procesar con managers correspondientes"
            }
            
            self._send_json_response(200, response)
            
        except Exception as e:
            print(f"Error en POST: {e}")
            response = {
                "error": "Error procesando POST",
                "details": str(e)
            }
            self._send_json_response(500, response)
    
    def do_PUT(self):
        self._send_json_response(200, {"message": "PUT recibido - Implementar"})
    
    def do_DELETE(self):
        self._send_json_response(200, {"message": "DELETE recibido - Implementar"})