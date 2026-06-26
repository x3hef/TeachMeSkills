# Задание 9

class Product:
    def __init__(self, name, quantity):
        self.name = name
        self._quantity = quantity

    @property
    def quantity(self):
        return self._quantity

    def add(self, amount):
        self._quantity += amount

    def remove(self, amount):
        if amount > self._quantity:
            print("Недостаточно товара!")
        else:
            self._quantity -= amount

    def info(self):
        print(f"{self.name}: {self._quantity}")


class Store:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def sell_product(self, name, amount):
        for p in self.products:
            if p.name == name:
                p.remove(amount)
                return
        print("Продукт не найден!")

    def show_products(self):
        for p in self.products:
            p.info()
