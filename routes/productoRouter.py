from fastapi import APIRouter, HTTPException
from models.models import Producto
from managers.productosManager import ProductosManager

router = APIRouter(prefix="/productos", tags=["Productos"])

@router.get("/")
def obtener_productos():
    return ProductosManager.obtener_todos()

@router.get("/{producto_id}")
def obtener_producto(producto_id: int):
    producto = ProductosManager.obtener_por_id(producto_id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@router.post("/")
def crear_producto(producto: Producto):
    return {"id": ProductosManager.crear(producto)}

@router.put("/{producto_id}")
def modificar_producto(producto_id: int, producto: Producto):
    ProductosManager.modificar(producto_id, producto)
    return {"mensaje": "Producto modificado"}

@router.delete("/{producto_id}")
def eliminar_producto(producto_id: int):
    ProductosManager.eliminar(producto_id)
    return {"mensaje": "Producto eliminado"}