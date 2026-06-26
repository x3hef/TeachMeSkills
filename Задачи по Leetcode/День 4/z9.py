# Задание 9

class Animal:
    def __init__(self, name: str):
        self._name = name

    def speak(self):
        print("Some Sound")

class Dog(Animal):
    def __init__(self, name: str):
        super().__init__(name)

    def speak(self):
        print("Wood!")

class Cat(Animal):
    def __init__(self, name: str):
        super().__init__(name)

    def speak(self):
        print("Meow!")


class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def show_animals(self):
        for animal in self.animals:
            print(animal)