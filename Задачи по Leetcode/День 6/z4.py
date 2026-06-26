# Задание 4

class Account:
    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self._balance = balance
        self.history = []

    @staticmethod
    def balance(new_balance: float):
        if isinstance(new_balance, (float, int)):
            if new_balance >= 0:
                return new_balance
        return None

    @property
    def depozit(self):
        return self._balance

    @depozit.setter
    def depozit(self, new_balance: float):
        if Account.balance(new_balance):
            self._balance += new_balance

    def withdraw(self, amount):
        if isinstance(amount, (float, int)):
            if amount >= 0:
                if self._balance - amount >= 0:
                    self._balance -= amount
            else:
                print("Error")
        else:
            print("Error")

    def transfer(self, other_account, amount):
        if amount > self.balance:
            print("Недостаточно средств")
        else:
            self.balance -= amount
            self.history.append(f"Перевод: -{amount} -> {other_account.owner}")
            other_account.balance += amount
            other_account.history.append(f"Получено: +{amount} от {self.owner}")

    def history(self):
        self.history.append("Пополнение: +100")
