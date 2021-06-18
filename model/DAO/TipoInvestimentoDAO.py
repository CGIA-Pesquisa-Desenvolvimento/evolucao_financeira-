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


class TipoInvestimentoDAO:

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

    def atualizar(c, d, id):
        """

        :param conn:
        :param categoria:
        :return:
        """

        query = "UPDATE tipo_investimento SET categoria = ?, descricao = ? WHERE id = ?"
        cur = conn.cursor()
        cur.execute(query, (c, d, id))
        conn.commit()

    def gravar(c, d):
        """

        :param conn:
        :param categoria:
        :return:
        """

        query = "INSERT INTO tipo_investimento (categoria, descricao) VALUES (?, ?)" #TODO Corrigir erro de conexão fechada com dois inserts consecutivos

        cur = conn.cursor()
        cur.execute(query, (c, d))
        conn.commit()
        conn.close()



    # TODO Adicionar try except nas funçoes sql


    def apagar(id):
        """

        :param conn:
        :param id:
        :return:
        """
        query = "DELETE FROM tipo_investimento WHERE ID = ?"

        cur = conn.cursor()
        cur.execute(query, (id,))
        conn.commit()

    def pesquisar(categoria=None):
        """

        :param conn:
        :param categoria:
        :return:
        """

        cur = conn.cursor()
        if categoria == None:
            cur.execute("SELECT * FROM tipo_investimento")
            result = cur.fetchall()
        else:
            cur.execute("SELECT * FROM tipo_investimento WHERE categoria = ?", categoria)
            result = cur.fechone()

        return result
