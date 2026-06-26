# Property

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance

    def delite_balance(self):
        del self.__balance

    balance = property(fget=get_balance, fset=set_balance)


b = BankAccount("BankAccount", 100)
b.set_balance(50)
print(b.get_balance())


