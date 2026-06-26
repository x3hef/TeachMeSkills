# Задание 5

class Product:
    def __init__(self, name: str, price: int, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def buy(self, amount: int) -> None:
        self.quantity -= amount
        if self.quantity <= 0:
            print("Недостаточно товара!")
        else:
            print(f"Товар куплен в количестве: {self.quantity}")


    def restock(self, amount: int) -> None:
        self.quantity += amount

    def info(self):
        print(f"Name: {self.name}, Price: {self.price},Quantity: {self.quantity}")


class Electronic(Product):
    def __init__(self, name, price, quantity, warranty):
        super().__init__(name, price, quantity)
        self.warranty = warranty

    def info(self):
        print(f"Name: {self.name}, Price: {self.price},Quantity: {self.quantity}, Warranty: {self.warranty}")


class Food(Product):
    def __init__(self, name, price, quantity, expiration_date):
        super().__init__(name, price, quantity)
        self.expiration_date = expiration_date

    def info(self):
        print(f"Name: {self.name}, Price: {self.price},Quantity: {self.quantity}", f"Expiration Date: {self.expiration_date}")

e = Electronic("iPhone", 1000, 5, 24)
f = Food("Milk", 2, 10, "2026-04-15")

e.info()  # iPhone - 1000$ - 5 шт - Гарантия: 24 мес
f.info()  # Milk - 2$ - 10 шт - Срок годности: 2026-04-15

e.buy(3)
e.info()  # Количество уменьшилось

f.restock(5)
f.info()  # Количество увеличилось