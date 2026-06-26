# Магические методы len и  abs

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __len___(self):
        return len(self.name + self.surname)

a = Person("Pasha", "Ser")
print(a.__len___())

class Otrezok:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        return abs(self)

    def __abs__(self):
        return abs(self.x - self.y)

x = Otrezok(60, 2)
print(x.__len__())