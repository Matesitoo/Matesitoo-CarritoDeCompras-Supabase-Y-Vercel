import os
import psycopg
from psycopg.rows import dict_row
from dotenv import load_dotenv

load_dotenv()

class Conexion:
    def __init__(self):
        self.conn = psycopg.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            row_factory=dict_row
        )

    def get_cursor(self):
        return self.conn.cursor()

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()