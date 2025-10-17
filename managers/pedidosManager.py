from datetime import datetime
from managers.conexionManagerSupabase import Conexion

class PedidosManager:

    @staticmethod
    def obtener_todos():
        con = Conexion()
        cur = con.get_cursor()
        cur.execute("SELECT * FROM pedidos")
        pedidos = cur.fetchall()
        con.close()
        return pedidos

    @staticmethod
    def obtener_por_id(pedido_id):
        con = Conexion()
        cur = con.get_cursor()
        cur.execute("SELECT * FROM pedidos WHERE id = %s", (pedido_id,))
        pedido = cur.fetchone()
        cur.execute("SELECT * FROM pedido_items WHERE pedido_id = %s", (pedido_id,))
        items = cur.fetchall()
        con.close()
        return {"pedido": pedido, "items": items}

    @staticmethod
    def obtener_por_cliente(cliente_id):
        con = Conexion()
        cur = con.get_cursor()
        cur.execute("SELECT * FROM pedidos WHERE cliente_id = %s", (cliente_id,))
        pedidos = cur.fetchall()
        con.close()
        return pedidos

    @staticmethod
    def crear(pedido):
        con = Conexion()
        cur = con.get_cursor()
        fecha = pedido.fecha or datetime.now()
        cur.execute(
            "INSERT INTO pedidos (cliente_id, fecha) VALUES (%s, %s) RETURNING id",
            (pedido.cliente_id, fecha)
        )
        pedido_id = cur.fetchone()["id"]

        for item in pedido.items:
            cur.execute(
                """INSERT INTO pedido_items 
                   (pedido_id, producto_id, cantidad, precio_unitario)
                   VALUES (%s, %s, %s, %s)""",
                (pedido_id, item.producto_id, item.cantidad, item.precio_unitario)
            )

        con.commit()
        con.close()
        return pedido_id