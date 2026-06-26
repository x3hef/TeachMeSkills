# Атрибуты экземпляра класса

class Car:
    model = "BMW"
    engine = 1

a1 = Car()
a2 = Car()
print(Car.__dict__)
print(a1.__dict__)
print(a2.__dict__)
print(a1.model)
print(a2.model)
a1.seet = 4
print(a1.seet)

