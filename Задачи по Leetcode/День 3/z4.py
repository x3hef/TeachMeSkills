# Задание 4

class User:
    total = 0

    def __init__(self, name: str, age: int):
        self.name = name
        self._age = age
        User.total += 1

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise ValueError("Возраст должен быть числом")

        if value < 0:
            raise ValueError("Возраст не может быть отрицательным")

        self._age = value

    @classmethod
    def total_user(cls):
        return cls.total
