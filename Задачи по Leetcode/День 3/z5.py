# Задание 5

class Product:

    def __init__(self, name: str, quantity: int):
        self.name = name
        self._quantity = quantity

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity: int):
        if not isinstance(quantity, int):
            raise ValueError
        if quantity < 0:
            raise ValueError("Количество не может быть отрицательным")

        self._quantity = quantity

    def add(self, amount: int):
        if not isinstance(amount, int):
            raise ValueError
        if amount <= 0:
            raise ValueError("Количество должно быть положительным")

        self._quantity += amount

    def remove(self, amount: int):
        if not isinstance(amount, int):
            raise ValueError

        if amount > self._quantity:
            print("Недостаточно товара")
        else:
            self._quantity -= amount

    @classmethod
    def create_empty(cls, name: str):
        return cls(name, 0)