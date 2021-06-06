import sqlite3
from sqlite3 import Error


def conection(db_file):
    conn = None

    try:
        conn = sqlite3.connect(db_file)

        return conn
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

