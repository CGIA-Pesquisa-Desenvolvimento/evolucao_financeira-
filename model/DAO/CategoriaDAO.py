import sqlite3
from  sqlite3 import Error
#from PyQt5.QtSql import QSqlQuery
#from database.conexao import conection
db = (r"C:\Users\carlos\OneDrive\Documentos\projetos\python\controle_financeiro\database\controle_financeiro.db")

#TODO Retirar este treche e usar função de conexão comum


def conection(db):
    conn = None

    try:
        conn = sqlite3.connect(db)

        return conn
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


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


def Gravar(conn, categoria):
    """

    :param conn:
    :param categoria:
    :return:
    """
    query = "INSERT INTO categoria(nome_categoria, obs) VALUES (?, ?)"

    cur = conn.cursor()
    cur.execute(query, categoria)
    conn.commit()
#TODO Adicionar try except nas funçoes sql


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


def Pesquisa(conn, categoria = None):
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
