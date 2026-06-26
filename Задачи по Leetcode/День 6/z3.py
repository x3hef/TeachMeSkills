# Задание 3

class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self._price = price

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, new_price: float):
        if isinstance(new_price, float):
            if new_price > 0:
                self._price = new_price
            else:
                print("Неверное значение ")
        else:
            print("Проверьте тип данных")

    def __str__(self):
        return f"Product: {self.name}, Price: {self._price}"


class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_total_product(self):
        total = 0
        for product in self.products:
            total += product.price

    def show_products(self):
        for product in self.products:
            print(product.name, product.price)
