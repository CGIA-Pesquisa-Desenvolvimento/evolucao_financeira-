import sqlite3
# from sqlite3 import Error

# from PyQt5.QtSql import QSqlQuery
# from database.conexao import conection
#from db import conexao

try:
    conn = sqlite3.connect('/home/carlos/Documentos/projetos/python/evolucao_financeira/db/controle_financeiro.db')


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

    def Atualizar(id, cat, obs):
        """

        :param conn:
        :param categoria:
        :return:
        """

        query = "UPDATE categoria SET nome_categoria = ?, obs = ? WHERE id = ?"
        cur = conn.cursor()
        cur.execute(query, (cat, obs, id))
        conn.commit()
        cur.close()
        conn.close()


    def Gravar(c, o):
        """

        :param conn:
        :param categoria:
        :return:
        """

        query = "INSERT INTO categoria (nome_categoria, obs) VALUES (?, ?)"

        cur = conn.cursor()
        cur.execute(query, (c, o))
        conn.commit()
        cur.close()
        conn.close()



    # TODO Adicionar try except nas funçoes sql


    def Apagar(id):
        """

        :param conn:
        :param id:
        :return:
        """
        query = "DELETE FROM categoria WHERE ID = ?"

        cur = conn.cursor()
        cur.execute(query, id)
        conn.commit()

    def Pesquisa(categoria=None):
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
