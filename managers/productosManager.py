from managers.conexionManagerSupabase import Conexion

class ProductosManager:

    @staticmethod
    def obtener_todos():
        con = Conexion()
        cur = con.get_cursor()
        cur.execute("SELECT * FROM productos")
        productos = cur.fetchall()
        con.close()
        return productos

    @staticmethod
    def obtener_por_id(producto_id):
        con = Conexion()
        cur = con.get_cursor()
        cur.execute("SELECT * FROM productos WHERE id = %s", (producto_id,))
        producto = cur.fetchone()
        con.close()
        return producto

    @staticmethod
    def crear(producto):
        con = Conexion()
        cur = con.get_cursor()
        cur.execute(
            "INSERT INTO productos (nombre, precio, stock) VALUES (%s, %s, %s) RETURNING id",
            (producto.nombre, producto.precio, producto.stock)
        )
        id_creado = cur.fetchone()["id"]
        con.commit()
        con.close()
        return id_creado

    @staticmethod
    def modificar(producto_id, producto):
        con = Conexion()
        cur = con.get_cursor()
        cur.execute(
            "UPDATE productos SET nombre = %s, precio = %s, stock = %s WHERE id = %s",
            (producto.nombre, producto.precio, producto.stock, producto_id)
        )
        con.commit()
        con.close()

    @staticmethod
    def eliminar(producto_id):
        con = Conexion()
        cur = con.get_cursor()
        cur.execute("DELETE FROM productos WHERE id = %s", (producto_id,))
        con.commit()
        con.close()