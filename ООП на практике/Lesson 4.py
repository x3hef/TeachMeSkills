# Функция как атрибут класса

class Car:
    model = "BMW"
    en = 1

    def drive(self):
        print("Функция")


с = Car()
с.drive()
