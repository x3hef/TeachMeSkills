# Задание 3

class Client:
    def __init__(self, name: str, balance: int) -> None:
        self.name = name
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if isinstance(value, int):
            if value >= 0:
                self._balance = value
            else:
                print("Баланс не может быть отрицательным!")
        else:
            raise TypeError

    def __str__(self):
        return self.name, self._balance


