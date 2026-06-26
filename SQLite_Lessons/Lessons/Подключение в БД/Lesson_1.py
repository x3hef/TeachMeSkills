# Lesson 1

import sqlite3 as sq

# con = sq.connect('test.db') # - соединение с бд или создание

with sq.connect('test.db') as con:
    cur = con.cursor() #Cursor

    # cur.execute("DROP TABLE IF EXISTS users")
    cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
    username INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL, 
    sex INTEGER DEFAULT 1, 
    age INTEGER NOT NULL, 
    score INTEGER
    )''')

