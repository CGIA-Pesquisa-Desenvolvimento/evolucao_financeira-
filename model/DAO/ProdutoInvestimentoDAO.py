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


class ProdutoInvestimentoDAO:

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

    def cadastrar(usuario):
        pass
        # conn = conexao
        # db = conn.conection()

    def atualizar(produto, descricao, id):
        """

        :param conn:
        :param categoria:
        :return:
        """

        query = "UPDATE produto_investimento SET produto = ?, descricao = ? WHERE id = ?"
        cur = conn.cursor()
        cur.execute(query, (produto, descricao, id))
        conn.commit()

    def gravar(produto, descricao):
        """

        :param conn:
        :param categoria:
        :return:
        """

        query = "INSERT INTO produto_investimento (produto, descricao) VALUES (?, ?)" #TODO Corrigir erro de conexão fechada com dois inserts consecutivos

        cur = conn.cursor()
        cur.execute(query, (produto, descricao))
        conn.commit()
        conn.close()



    # TODO Adicionar try except nas funçoes sql


    def apagar(id):
        """

        :param conn:
        :param id:
        :return:
        """
        query = "DELETE FROM produto_investimento WHERE ID = ?"

        cur = conn.cursor()
        cur.execute(query, (id,))
        conn.commit()

    def pesquisar(produto=None):
        """

        :param conn:
        :param categoria:
        :return:
        """

        cur = conn.cursor()
        if produto == None:
            cur.execute("SELECT * FROM produto_investimento")
            result = cur.fetchall()
        else:
            cur.execute("SELECT * FROM produto_investimento WHERE produto = ?", produto)
            result = cur.fechone()

        return result
