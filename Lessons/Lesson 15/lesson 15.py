import sqlite3  # - норм для локальных тестах

#
connection = sqlite3.connect("test.db")

connection.execute("""
    CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);""")
