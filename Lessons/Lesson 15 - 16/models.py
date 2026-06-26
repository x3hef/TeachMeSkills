from database import cursor,conn


class Users:

    @staticmethod
    def is_exists(username):
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        return cursor.fetchone() is not None

    @staticmethod
    def create(username, password):
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password)
        )
        conn.commit()

    @staticmethod
    def get(username, password):
        cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        )
        return cursor.fetchone()

    @staticmethod
    def add_points(user_id, amount):
        cursor.execute(
            "UPDATE users SET points = points + ? WHERE id=?",
            (amount, user_id)
        )
        conn.commit()

    @staticmethod
    def get_points(user_id):
        cursor.execute("SELECT points FROM users WHERE id=?", (user_id,))
        return cursor.fetchone()[0]


class Products:

    @staticmethod
    def all():
        cursor.execute("SELECT * FROM products")
        return cursor.fetchall()

    @staticmethod
    def get(product_id):
        cursor.execute("SELECT * FROM products WHERE id=?", (product_id,))
        return cursor.fetchone()

class Tickets:

    @staticmethod
    def create():
        import uuid
        ticket = str(uuid.uuid4())

        cursor.execute(
            "INSERT INTO tickets (uuid, available, user_id) VALUES (?, ?, ?)",
            (ticket, 1, None)
        )
        conn.commit()

        return ticket

    @staticmethod
    def valid_ticket(ticket_uuid):
        cursor.execute(
            "SELECT * FROM tickets WHERE uuid=?",
            (ticket_uuid,)
        )
        ticket = cursor.fetchone()

        if not ticket:
            return False

        if ticket[1] == 0:
            return False

        return True

    @staticmethod
    def use(ticket_uuid, user_id):
        cursor.execute(
            "UPDATE tickets SET available=0, user_id=? WHERE uuid=?",
            (user_id, ticket_uuid)
        )
        conn.commit()

class Orders:

    @staticmethod
    def create(user_id, product_id, quantity):
        cursor.execute(
            "INSERT INTO orders (user_id, product_id, quantity) VALUES (?, ?, ?)",
            (user_id, product_id, quantity)
        )
        conn.commit()

    @staticmethod
    def get_user_orders(user_id):
        cursor.execute("""
            SELECT products.name, orders.quantity
            FROM orders
            JOIN products ON orders.product_id = products.id
            WHERE orders.user_id=?
        """, (user_id,))
        return cursor.fetchall()