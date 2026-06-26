# Задание 6

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def depozit(self, amount: int):
        self.balance += amount
        print(f"Баланс пополнен на {amount}")

    def withdraw(self, amount: int):
        if self.balance < 0:
            print("Недостаточно денег")
        else:
            self.balance -= amount
            print(f"Баланс пополнен на {amount}")

    def info(self):
        print(f"Имя владельца {self.owner}, Баланс счета {self.balance}")


class SavingsAccount:
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance += self.balance * self.interest_rate / 100
        print(f"Баланс после начисления процентов: {self.balance}")
        