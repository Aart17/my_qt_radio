import os.path
import sys
import sqlite3
from sqlite3 import Error


def sql_con(db_filename):
    try:
        conn = sqlite3.connect(db_filename)
        return conn
    except Error:
        print(Error)


def sql_table(conn, table_name):
    curs = conn.cursor()
    curs.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ('
                 'id integer PRIMARY KEY AUTOINCREMENT,'
                 'name text ,'
                 'frequency real UNIQUE,'
                 'URL text)')

    conn.commit()


def sql_create(conn, table_name, entity):
    curs = conn.cursor()
    curs.execute(f'INSERT INTO {table_name}(name, frequency, URL) VALUES(?, ?, ?)', entity)
    conn.commit()


def check_fm(con, name, dct):
    curs = con.cursor()
    try:
        curs.execute(f'INSERT INTO {name}(frequency) VALUES(?)', dct)
    except sqlite3.IntegrityError:
        print("error")


def check(con, name, log):
    curs = con.cursor()
    curs.execute(f"SELECT frequency FROM {name} WHERE frequency={log}")
    print(curs.fetchone())
    if curs.fetchone() is None:
        k = True
        con.commit()
        return k
    else:
        k = False
        con.commit()
        return k


def add_insert_func(con, dct, table_name, flag=False):
    curs = con.cursor()
    try:
        curs.execute(f'INSERT INTO {table_name}(frequency, name, URl) VALUES(?, ?, ?)', dct)
        if flag is True:
            k = False
    except sqlite3.IntegrityError:
        if flag is True:
            k = True
    con.commit()
    if flag is True:
        return k


def check_added_radio():
    if os.path.exists('radioDataBase.db'):
        con = sqlite3.connect('radioDataBase.db')
        curs = con.cursor()
        curs.execute('SELECT * FROM added_radio')
        if curs.fetchone() is None:
            k = False
            con.commit()
            return k
        else:
            k = True
            con.commit()
            return k


def insert_func(con, k, table_name):
    for i in k:
        url = k[i][0]
        name = k[i][1]
        dct = [i, name, url]
        curs = con.cursor()
        try:
            curs.execute(f'INSERT INTO {table_name}(frequency, name, URl) VALUES(?, ?, ?)', dct)
        except sqlite3.IntegrityError:
            pass
        con.commit()
