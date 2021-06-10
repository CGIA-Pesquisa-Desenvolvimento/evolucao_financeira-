import sqlite3
from sqlite3 import Error

#db_file = (r"/home/carlos/Documentos/projetos/python/evolucao_financeira/controle_financeiro.db")


class ConexaoDB:

    def conection(self):
        conn = None

        try:
            conn = sqlite3.connect('controle_financeiro.db')

            return conn
        except Error as e:
            # TODO escrever mensagem de erro no log.txt
            print(e)
        finally:
            if conn:
                conn.close()


# class ConexaoDB:
#
#     def __init__(self, banco = None):
#         self.conn = None
#         self.cursor = None
#
#         if banco:
#             self.conectar(banco)
#
#     def conectar(self, banco):
#         try:
#             self.conn = sqlite3.connect(banco)
#             self.cursor = self.conn.cursor()
#
#         except sqlite3.Error as e:
#             pass
