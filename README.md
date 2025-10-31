#Carrito de Compras API

API para gestion de carrito de compras

#Caracteristicas

- Gestion de clientes, productos y pedidos
- Base de datos PostgreSQL con Supabase
- Despliegue en Vercel
- Validación de datos con Pydantic

#API Endpoints

#Clientes
- `GET /clientes` - Listar todos los clientes
- `GET /clientes/{id}` - Obtener cliente por ID  
- `POST /clientes` - Crear nuevo cliente
- `PUT /clientes/{id}` - Actualizar cliente
- `DELETE /clientes/{id}` - Eliminar cliente

#Productos
- `GET /productos` - Listar todos los productos
- `GET /productos/{id}` - Obtener producto por ID
- `POST /productos` - Crear nuevo producto
- `PUT /productos/{id}` - Actualizar producto
- `DELETE /productos/{id}` - Eliminar producto

#Pedidos
- `GET /pedidos` - Listar todos los pedidos
- `GET /pedidos/{id}` - Obtener pedido con items y total
- `GET /pedidos/cliente/{cliente_id}` - Pedidos por cliente ID
- `GET /pedidos/cliente_nombre/{nombre}` - Pedidos por nombre de cliente
- `GET /pedidos/filtrar?desde=YYYY-MM-DD&hasta=YYYY-MM-DD` - Filtrar por fecha
- `POST /pedidos` - Crear nuevo pedido con items

#Instalacion Local

1. Clonar repositorio:
```bash
git clone <url-del-repositorio>
cd CARRITO_API