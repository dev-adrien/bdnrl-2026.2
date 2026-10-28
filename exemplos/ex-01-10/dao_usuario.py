from db import get_connection
from modelo import Usuario

class UsuarioDAO:
    def __init__(self): self.conn = get_connection()
    self._criar_tabela()

    def _criar_tabela(self):
        cursor = self.conn.cursor()

    cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS usuarios 
    ( id INTEGER PRIMARY KEY AUTOINCREMENT, 
    nome TEXT NOT NULL) """)

    self.conn.commit()