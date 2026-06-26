from database import cursor, conn  # type: ignore[attr-defined]


# ТАБЛИЦА ПОЛЬЗОВАТЕЛЕЙ
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    points INTEGER DEFAULT 0 
    )
''')

# ТАБЛИЦА ТОВАРОВ
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT, 
    price INTEGER
)
''')

# ТАБЛИЦА ТИКЕТОВ
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tickets (
    uuid TEXT PRIMARY KEY,  
    available INTEGER,      
    user_id INTEGER
    )  
''')

# Таблица заказов
cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,        
    product_id INTEGER,     
    quantity INTEGER         
)
""")

conn.commit()

cursor.execute("SELECT COUNT(*) FROM products")

if cursor.fetchone()[0] ==  0:
    cursor.executemany("INSERT INTO products (name, price) VALUES (?, ?)",
        [
            ("Телефон", 100),
            ("Ноутбук", 300),
            ("Наушники", 50)
        ]
    )

    conn.commit()

