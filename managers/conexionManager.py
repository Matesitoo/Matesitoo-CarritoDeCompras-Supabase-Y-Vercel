import sqlite3

class Conexion:
    def __init__(self):
        self.conn = sqlite3.connect("carrito.db")
        self.conn.row_factory = sqlite3.Row

    def get_cursor(self):
        return self.conn.cursor()

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()