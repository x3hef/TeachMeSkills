# Методы класса (classmethod) и статические методы @staticmethod

#Функция classmethod(function) в Python используется для создания методов класса.
# Методы класса принимают в качестве первого аргумента сам класс,
# а не экземпляр класса. Это полезно, когда нужно работать с самим классом,
# а не с его конкретным экземпляром.


class MyClass:
    class_variable = "Hello World"

    def __init__(self, instance):
        self.instance = instance

    @classmethod
    def class_method(cls):
        print(cls.class_variable)


# Методы класса часто используются как альтернативные конструкторы.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        current_year = 2020
        age = current_year - birth_year
        return cls(name, age)


person = Person.from_birth_year("Bob", 18)
print(person.name)
print(person.age)


# Функция staticmethod в Python используется для создания статических
# методов внутри классов. Статические методы не требуют
# создания экземпляра класса и не получают ни первого аргумента self,
# ни первого аргумента cls. Они могут быть вызваны непосредственно
# через сам класс.


# Создание и использование статического метода
class MyClass2():
    @staticmethod
    def static_method():
        print("это статический метод")

MyClass2.static_method()

# Статические методы с параметрами

class MathOperation:
    @staticmethod
    def add(a, b):
        return a + b

result = MathOperation.add(1, 2)
print(result)