# Множественное наследование

class Doctor:

    def sleep(self):
        print("sleep")

class Pepper:

    def sleep(self):
        print("sleep")

class People(Pepper,Doctor):
    pass


print(People.__mro__)
# - (<class '__main__.People'>, <class '__main__.Pepper'>, <class '__main__.Doctor'>, <class 'object'>)