from fastapi import FastAPI
from routes.clientRouter import router as cliente_router
from routes.productoRouter import router as producto_router
from routes.pedidoRouter import router as pedido_router

app = FastAPI(title="Carrito de Compras API")

app.include_router(cliente_router)
app.include_router(producto_router)
app.include_router(pedido_router)

@app.get("/")
def root():
    return {"mensaje": "API de carrito de compras activa"}