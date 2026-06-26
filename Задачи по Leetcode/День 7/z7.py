# Задание 7

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

