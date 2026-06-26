import sqlite3

connection = sqlite3.connect('test1.db')
cursor = connection.cursor()

# connection.execute("""
#     CREATE TABLE articles (
#     title text,
#     full_text text,
#     views integer,
#     avtor text
#     )
# """)

# cursor.execute("INSERT INTO articles VALUES ('Facebook is cool', 'Facebook', '100', 'admin2')")
cursor.execute("SELECT title FROM articles")
# cursor.execute("SELECT rowid, title FROM articles")
# print(cursor.fetchall())
print(cursor.fetchmany())
print(cursor.fetchone())
item = cursor.fetchone()
# cursor.execute("delete from articles where title='{}'".format(item[0]))

for el in item:
    print(el)


connection.commit()
connection.close()
