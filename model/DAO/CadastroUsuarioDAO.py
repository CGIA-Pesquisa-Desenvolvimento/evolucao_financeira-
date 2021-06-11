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


class CadastroUsuarioDAO:

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

    def atualizar(n, e, s, id):
        """

        :param conn:
        :param categoria:
        :return:
        """

        query = "UPDATE usuario SET nome = ?, email = ?, senha = ? WHERE id = ?"
        cur = conn.cursor()
        cur.execute(query, (n, e, s, id))
        conn.commit()


    def gravar(n, e, s):
        """

        :param conn:
        :param categoria:
        :return:
        """

        query = "INSERT INTO usuario (nome_usuario, email, senha) VALUES (?, ?, ?)"

        cur = conn.cursor()
        cur.execute(query, (n, e, s))
        conn.commit()
        conn.close()



    # TODO Adicionar try except nas funçoes sql


    def apagar(id):
        """

        :param conn:
        :param id:
        :return:
        """
        query = "DELETE FROM usuario WHERE ID = ?"

        cur = conn.cursor()
        cur.execute(query, (id,))
        conn.commit()

    def pesquisar(usuario=None):
        """

        :param conn:
        :param categoria:
        :return:
        """

        cur = conn.cursor()
        if usuario == None:
            cur.execute("SELECT * FROM usuario")
            result = cur.fetchall()
        else:
            cur.execute("SELECT * FROM usuario WHERE nome_usuario = ?", usuario)
            result = cur.fechone()

        return result
