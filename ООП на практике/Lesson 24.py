# Наследование переопределение методов

class Person:
    def breathe(self):
        print("Breathe")
    def walk(self):
        print("Walk")

class Student(Person):
    def breathe(self):
        print("2")


