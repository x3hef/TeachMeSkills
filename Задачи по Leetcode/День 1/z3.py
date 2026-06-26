# Задание 3

class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def is_adult(self):
        if self.age >= 18:
            return True
        else:
            return False


class Counter:
    def __init__(self, value: int):
        self.value = value

    def inc(self):
        self.value += 1

    def dec(self):
        self.value -= 1

    def reset(self):
        self.value = 0

