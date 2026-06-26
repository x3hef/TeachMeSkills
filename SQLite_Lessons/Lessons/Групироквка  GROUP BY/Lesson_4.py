import sqlite3 as sq

with sq.connect('test.db') as con:
    cur = con.cursor()

    cur.execute('''
    CREATE TABLE games (
        user_id INTEGER NOT NULL PRIMARY KEY,
        score INTEGER,
        time INTEGER DEFAULT 0
    )
    ''')

    cur.execute('''
    CREATE TABLE users (
        name TEXT,
        age INTEGER DEFAULT 0,
        score INTEGER DEFAULT 0
    )
    ''')