from loader import loading_screen
from models import Users, Products, Tickets, Orders

current_user = None

def main():
    loading_screen()

if __name__ == "__main__":
    main()

def show_products():
    products = Products.all()
    print("\nСписок товаров:")
    for p in products:
        print(f"{p[0]:<5} {p[1]:<20} {p[2]}")


def register():
    global current_user

    username = input("Логин: ")
    password = input("Пароль: ")

    if Users.is_exists(username):
        print("Пользователь уже есть")
        return

    Users.create(username, password)
    current_user = Users.get(username, password)

    print("Регистрация успешна!")


def login():
    global current_user

    username = input("Логин: ")
    password = input("Пароль: ")

    user = Users.get(username, password)

    if user:
        current_user = user
        print("Вход выполнен!")
    else:
        print("Неверные данные")


def create_ticket():
    ticket = Tickets.create()
    print("Тикет:", ticket)


def use_ticket():
    ticket_uuid = input("Введите тикет: ")

    if not Tickets.valid_ticket(ticket_uuid):
        print("Неверный или использованный тикет")
        return

    Tickets.use(ticket_uuid, current_user[0])
    Users.add_points(current_user[0], 20)

    print("Тикет применен! +20 поинтов")


def buy():
    product_id = int(input("ID товара: "))
    quantity = int(input("Количество: "))

    product = Products.get(product_id)

    if not product:
        print("Товар не найден")
        return

    total_price = product[2] * quantity
    points = Users.get_points(current_user[0])

    if points < total_price:
        print("Недостаточно поинтов")
        return

    Users.add_points(current_user[0], -total_price)
    Orders.create(current_user[0], product_id, quantity)

    print("Покупка успешна!")


def profile():
    points = Users.get_points(current_user[0])
    print(f"\nПоинты: {points}")

    orders = Orders.get_user_orders(current_user[0])

    print("Покупки:")
    for o in orders:
        print(o[0], "x", o[1])


# ---------------- МЕНЮ ----------------

while True:
    print("\n--- МЕНЮ ---")
    print("1. Товары")
    print("2. Регистрация")
    print("3. Вход")
    print("4. Создать тикет")
    print("5. Использовать тикет")
    print("6. Купить")
    print("7. Профиль")
    print("0. Выход")

    cmd = input("Выберите: ")

    if cmd == "1":
        show_products()

    elif cmd == "2":
        register()

    elif cmd == "3":
        login()

    elif cmd == "4":
        create_ticket()

    elif cmd == "5":
        if current_user:
            use_ticket()
        else:
            print("Сначала войдите")

    elif cmd == "6":
        if current_user:
            buy()
        else:
            print("Сначала войдите")

    elif cmd == "7":
        if current_user:
            profile()
        else:
            print("Сначала войдите")

    elif cmd == "0":
        break
