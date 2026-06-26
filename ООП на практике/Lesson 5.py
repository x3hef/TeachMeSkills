# Моносостояние

class Cat:
    breed = "pers"


a = Cat()
print(a.breed)
b = Cat()
print(b.breed)

class Cat2:
    __shared_attr = {
        "breed": "pers",
        "color": "blue"
    }

    def __init__(self, breed, color):
        self.__dict__ = Cat.__shared_attr
    