import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0152",
    database="lesson14"
)

cursor = db.cursor()

cursor.execute("SELECT * FROM users")

for row in cursor:  # type: ignore[union-attr]
    print(row)