import pymysql
from config import *

try:
    conn = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        with conn.cursor() as cursor:
            create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        phone VARCHAR(255)
)
"""
            cursor.execute(create_table_query)
            print("Table created")

        # insert data
        with conn.cursor() as cursor:
            insert_query = """ 
            INSERT INTO users (name, phone) VALUES ('Anya', '8012334324')
            """
            cursor.execute(insert_query)
            conn.commit()
            print("Table inserted")
            with conn.cursor() as cursor:
                select_query = """SELECT * FROM users"""
                cursor.execute(select_query)
                for row in cursor.fetchall():  # извлечь все строки!!!
                    print(row)

        # delete data
        with conn.cursor() as cursor:
            select_query = """DELETE FROM users WHERE name = 'Anya'"""
            cursor.execute(select_query)
            conn.commit()

        # drop[ table:
        with conn.cursor() as cursor:
            delete_query = """DROP TABLE users'"""

    finally:
        conn.close()
except Exception as ex:
    print("Error", ex)
finally:
    print("Done")
