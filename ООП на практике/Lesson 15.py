# магические методы add mul sub truediv

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __add__(self, other):
        return self.balance + other

    def __radd__(self, other):
        return self.balance + other

    def __mul__(self, other):
        return self.balance * other

m = BankAccount("Mr", 100)
print(m + 100)
print(m.balance)
t = BankAccount("T", 200)
print(t)
print(12 + t)
print(m.balance)