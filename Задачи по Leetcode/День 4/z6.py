# Задание 6

class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self._price = price

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price < 0:
            print("Ошибка!")
        else:
            self._price = new_price

    def __str__(self):
        print(f"Product(name={self.name}, price={self._price})")

class DiscountedProduct(Product):
    def __init__(self, name: str, price: float, discount = 10):
        super().__init__(name, price)
        self._discount = discount

    def get_discounted_price(self):
        return self.price * (1 - self._discount / 100)
