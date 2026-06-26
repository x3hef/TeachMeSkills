# Задание 2

class Product:
    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity

    def add_stock(self, amount: int):
        if isinstance(amount, int):
            self.quantity += amount
        else:
            raise TypeError

    def remove_stock(self, amount: int):
        if isinstance(amount, int):
            if amount > 0:
                if amount <= self.quantity:
                    self.quantity -= amount
                else:
                    print("Ошибка")
            else:
                print("Не может быть меньше нуля!")
        else:
            raise TypeError

    def __str__(self):
        return f"Product(name={self.name}, quantity={self.quantity})"


class Warehouse:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_product(self, name):
        for product in self.products:
            if product.name == name:
                return product
        return None

    def show_products(self):
        for product in self.products:
            print(product.name)



