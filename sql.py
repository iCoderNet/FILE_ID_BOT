import sqlite3
from aiogram import types

def sql_code(text):
    try:
        with sqlite3.connect('db.sqlite3') as conn:
            cur = conn.cursor()
            r = cur.execute(text)
            conn.commit()
            return r.fetchall()
    except Exception as e:
        return e