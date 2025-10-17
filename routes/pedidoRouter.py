from fastapi import APIRouter, HTTPException, Query
from models.models import Pedido
from managers.pedidosManager import PedidosManager
from managers.clientesManager import ClientesManager
from managers.conexionManagerSupabase import Conexion
from datetime import datetime

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])

@router.get("/")
def obtener_pedidos():
    return PedidosManager.obtener_todos()

@router.get("/{pedido_id}")
def obtener_pedido(pedido_id: int):
    pedido = PedidosManager.obtener_por_id(pedido_id)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")

    total = sum(item["cantidad"] * item["precio_unitario"] for item in pedido["items"])

    return {
        "pedido": pedido["pedido"],
        "items": pedido["items"],
        "total": total
    }

@router.get("/cliente/{cliente_id}")
def obtener_por_cliente(cliente_id: int):
    return PedidosManager.obtener_por_cliente(cliente_id)

@router.post("/")
def crear_pedido(pedido: Pedido):
    pedido_id = PedidosManager.crear(pedido)
    return {"id": pedido_id}

@router.get("/cliente_nombre/{nombre}")
def obtener_por_nombre(nombre: str):
    clientes = ClientesManager.obtener_todos()
    cliente = next((c for c in clientes if c["nombre"].lower() == nombre.lower()), None)

    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")

    return PedidosManager.obtener_por_cliente(cliente["id"])

@router.get("/filtrar")
def filtrar_por_fecha(
    desde: str = Query(..., description="Fecha inicio (YYYY-MM-DD)"),
    hasta: str = Query(..., description="Fecha fin (YYYY-MM-DD)")
):
    try:
        fecha_desde = datetime.strptime(desde, "%Y-%m-%d")
        fecha_hasta = datetime.strptime(hasta, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(status_code=400, detail="Formato de fecha inválido")

    con = Conexion()
    cur = con.get_cursor()
    cur.execute(
        "SELECT * FROM pedidos WHERE fecha BETWEEN %s AND %s",
        (fecha_desde, fecha_hasta)
    )
    filas = cur.fetchall()
    con.close()

    # Convertir filas a lista de diccionarios para JSON
    pedidos = [dict(fila) for fila in filas]

    return pedidos