# Задание 8

class Car:
    def __init__(self, brand: str, speed: int) -> None:
        self.brand = brand
        self.speed = speed

    def accelerate(self, amount: int):
        if amount > 0:
            if amount + self.speed <= 180:
                self.speed += amount
            else:
                print("Скорость не может быть больше 180 км/ч")
        else:
            print("Скорость не может быть отрицательной!")

    def brake(self, amount: int):
        if self.speed - amount < 0:
            self.speed = 0
        else:
            self.speed -= amount

    def __str__(self):
        return f"{self.brand}, {self.speed}"


class ElectricCar(Car):
    def __init__(self, brand, speed, battery):
        super().__init__(brand, speed)
        self.battery = battery  # уровень заряда 0–100

    def charge(self, amount):
        if amount < 0:
            print("Ошибка: отрицательный заряд!")
            return
        self.battery += amount
        if self.battery > 100:
            self.battery = 100

    def __str__(self):
        return f"{self.brand}, {self.speed} км/ч, Заряд: {self.battery}%"