# Command SELECT and INSERT

# AND - условное И: exp1 AND exp2. Истинное, если одновременно истинны exp1 and exp2
# OR - условие ИЛИ
# NOT - условное НЕ
# IN - вхождение во множество значений
# NOT IN - не вхождение во множество значений

import sqlite3 as sq

with sq.connect('test.db') as conn:
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
    username INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL, 
    sex INTEGER DEFAULT 1, 
    age INTEGER NOT NULL, 
    score INTEGER
    )''')

    cur.execute("SELECT * FROM users WHERE score > 100 ORDER BY score DESC LIMIT 2")
    result = cur.fetchall() # получение результата отбора
    print(result)