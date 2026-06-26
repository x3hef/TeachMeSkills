# Атрибуты класса - данные класса
# получать доступ к атрибутам класса
# изменять атрибуты класса
# удалять атрибуты класса

class Person:
    name = 'Ivan'
    age = 20

print(Person.name)
print(Person.age)
print(Person.__dict__) # - mappinqproxy
print(getattr(Person, 'name1', 1000))
print(getattr(Person, 'name', 1000))
Person.age = 30
print(Person.age)
Person.x = 100
del Person.x
print(Person.__dict__)