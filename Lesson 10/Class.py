import time


class Auto:

    def __init__(self, brand, age, mark, color=None, weight=None):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight

    def move(self):
        print("move")

    def stop(self):
        print("stop")

    def birthday(self):
        self.age += 1


class Truck(Auto):

    def __init__(self, brand, age, mark, max_load, color=None, weight=None):
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self):
        print("attention")
        super().move()

    def load(self):
        time.sleep(1)
        print("load")
        time.sleep(1)


class Car(Auto):

    def __init__(self, brand, age, mark, max_speed, color=None, weight=None):
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f"max speed is {self.max_speed}")


truck1 = Truck("Volvo", 5, "T1", 10000, "white", 8000)
truck2 = Truck("MAN", 3, "T2", 12000, "blue", 8500)


car1 = Car("BMW", 2, "X5", 250, "black", 2000)
car2 = Car("Audi", 4, "A6", 240, "gray", 2100)


truck1.move()
truck1.load()
truck1.stop()
truck1.birthday()
print(truck1.age)


truck2.move()
truck2.load()


car1.move()
car1.stop()
car1.birthday()
print(car1.age)

car2.move()
car2.stop()