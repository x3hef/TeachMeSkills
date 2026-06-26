# Задание

class Vehicle:
    def __init__ (self, brand: str, year: int, mileage: int ):
        self.brand = brand
        self.year = year
        self.mileage = mileage

    def drive(self, km: str):
        self.mileage += km

    def info(self):
        print(f"{self.brand} {self.year} {self.mileage}")
