# Делегирование

class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def life(self):
        print("life")

class Student(Person):

    def __init__(self, subject):
        super().__init__(name="",age=0)
        self.subject = subject

    def life(self):
        print("life")
        super().life()


