from managers.conexionManagerSupabase import Conexion

class ClientesManager:

    @staticmethod
    def obtener_todos():
        con = Conexion()
        cur = con.get_cursor()
        cur.execute("SELECT * FROM clientes")
        clientes = cur.fetchall()
        con.close()
        return clientes

    @staticmethod
    def obtener_por_id(cliente_id):
        con = Conexion()
        cur = con.get_cursor()
        cur.execute("SELECT * FROM clientes WHERE id = %s", (cliente_id,))
        cliente = cur.fetchone()
        con.close()
        return cliente

    @staticmethod
    def crear(cliente):
        con = Conexion()
        cur = con.get_cursor()
        cur.execute(
            "INSERT INTO clientes (nombre, email) VALUES (%s, %s) RETURNING id",
            (cliente.nombre, cliente.email)
        )
        id_creado = cur.fetchone()["id"]
        con.commit()
        con.close()
        return id_creado

    @staticmethod
    def modificar(cliente_id, cliente):
        con = Conexion()
        cur = con.get_cursor()
        cur.execute(
            "UPDATE clientes SET nombre = %s, email = %s WHERE id = %s",
            (cliente.nombre, cliente.email, cliente_id)
        )
        con.commit()
        con.close()

    @staticmethod
    def eliminar(cliente_id):
        con = Conexion()
        cur = con.get_cursor()
        cur.execute("DELETE FROM clientes WHERE id = %s", (cliente_id,))
        con.commit()
        con.close()