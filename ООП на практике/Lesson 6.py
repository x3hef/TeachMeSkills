# Уровни доступа

class BankAccount:
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = balance
        self.password = password

    def print_data(self):
        print(self.name)
        print(self.balance)
        print(self.password)

account1  = BankAccount("BankAcount", 100, 100)

account1.print_data()


