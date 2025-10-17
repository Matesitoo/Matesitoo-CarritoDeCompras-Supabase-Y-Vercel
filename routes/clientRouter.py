from fastapi import APIRouter, HTTPException
from models.models import Cliente
from managers.clientesManager import ClientesManager

router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.get("/")
def obtener_clientes():
    return ClientesManager.obtener_todos()

@router.get("/{cliente_id}")
def obtener_cliente(cliente_id: int):
    cliente = ClientesManager.obtener_por_id(cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente

@router.post("/")
def crear_cliente(cliente: Cliente):
    return {"id": ClientesManager.crear(cliente)}

@router.put("/{cliente_id}")
def modificar_cliente(cliente_id: int, cliente: Cliente):
    ClientesManager.modificar(cliente_id, cliente)
    return {"mensaje": "Cliente modificado"}

@router.delete("/{cliente_id}")
def eliminar_cliente(cliente_id: int):
    ClientesManager.eliminar(cliente_id)
    return {"mensaje": "Cliente eliminado"}