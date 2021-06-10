import sqlite3
# from sqlite3 import Error

# from PyQt5.QtSql import QSqlQuery
# from database.conexao import conection
#from db import conexao

try:
    conn1 = sqlite3.connect('/home/carlos/Documentos/projetos/python/evolucao_financeira/db/controle_financeiro.db')


except sqlite3.Error as e:
    # TODO escrever mensagem de erro no log.txt
    print(e)


# TODO Retirar este treche e usar função de conexão comum


class CategoriaDAO:

    # def conection(db):
    #     conn = None
    #
    #     try:
    #         conn = sqlite3.connect(db)
    #
    #         return conn
    #     except Error as e:
    #         print(e)
    #     finally:
    #         if conn:
    #             conn.close()

    def cadastrar_categoria(categoria):
        pass
        # conn = conexao
        # db = conn.conection()

    def Atualizar(conn, categoria):
        """

        :param conn:
        :param categoria:
        :return:
        """

        query = "UPDATE categoria SET nome_categoria = ?, obs = ? WHERE id = ?"
        cur = conn.cursor()
        cur.execute(query, categoria)
        conn.commit()


    def Gravar(c, o):
        """

        :param conn:
        :param categoria:
        :return:
        """
     #   conn = conexao
      #  db = conn1.
      #   ca = cta
      #   type(cta)
        query = "INSERT INTO categoria (nome_categoria, obs) VALUES (?, ?)"

        cur = conn1.cursor()
        cur.execute(query, (c, o))
        conn1.commit()
        conn1.close()



    # TODO Adicionar try except nas funçoes sql


    def Apagar(conn, id):
        """

        :param conn:
        :param id:
        :return:
        """
        query = "DELETE FROM categoria WHERE ID = ?"

        cur = conn.cursor()
        cur.execute(query, (id,))
        conn.commit()

    def Pesquisa(conn, categoria=None):
        """

        :param conn:
        :param categoria:
        :return:
        """

        cur = conn.cursor()
        if categoria == None:
            cur.execute("SELECT * FROM categoria")
            result = cur.fetchall()
        else:
            cur.execute("SELECT * FROM categoria WHERE nome_categoria = ?", categoria)
            result = cur.fechone()

        return result
