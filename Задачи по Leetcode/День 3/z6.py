# Задание 6

class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self._price = price

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print("Нельзя ставить такую цену")
        else:
            self._price = new_price

    def info(self):
        print(f"{self.name}: {self._price}")




