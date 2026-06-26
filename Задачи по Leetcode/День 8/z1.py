# Задание 1

class BankAccount:
    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self._balance = balance

    @property
    def balance(self) -> float:
        return self._balance
    @balance.setter
    def balance(self, new_balance: float):
        if new_balance > 0:
            self._balance += new_balance
            print(f"Баланс увеличен на {new_balance}")
        if new_balance < 0:
            if self._balance - new_balance < 0:
                print("Недостаточно денег")
            self._balance -= new_balance
            print(f"Баланс уменьшен на {new_balance}")

