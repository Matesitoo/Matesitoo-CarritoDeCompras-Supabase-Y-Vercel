from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class Cliente(BaseModel):
    nombre: str
    email: str

class ClienteOut(Cliente):
    id: int

class Producto(BaseModel):
    nombre: str
    precio: float
    stock: int

class ProductoOut(Producto):
    id: int

class PedidoItem(BaseModel):
    producto_id: int
    cantidad: int
    precio_unitario: float

class Pedido(BaseModel):
    cliente_id: int
    fecha: Optional[datetime] = None
    items: List[PedidoItem]

class PedidoOut(BaseModel):
    id: int
    cliente_id: int
    fecha: datetime
    items: List[PedidoItem]