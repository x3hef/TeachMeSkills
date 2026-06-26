# Задание 8

class Product:
    def __init__(self, name: str, price: float):
        self._name = name
        self._price = price

    @property
    def prices(self):
        return self._price

    @prices.setter
    def prices(self, new_price: float):
        if isinstance(new_price, float):
            self._price = new_price
        else:
            raise TypeError

    def __str__(self):
        return f"Product: {self._name}, - {self._price}"

class Cart:
    def __init__(self, products: list):
        self.products = products

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_total_price(self):
        return sum(product.prices for product in self.products)

    def show_products(self):
        print(self.products)


