# Задание 1
class Soda:
    def __init__(self, additive: str):
        self.additive = additive

    def show_my_drink(self, additive):
        self.additive = additive
        if self.additive != "":
            print(f"Газировка и {self.additive}")
        else:
            print("Обычная газировка")


# Задание 2
class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if not all(isinstance(i, (int, float)) for i in [self.a, self.b, self.c]):
            return "Нужно вводить только числа!"
        elif self.a <= 0 or self.b <= 0 or self.c <= 0:
            return "С отрицательными числами ничего не выйдет!"
        if self.a + self.b > self.c and \
                self.a + self.c > self.b and \
                self.b + self.c > self.a:
            return "Ура, можно построить треугольник!"
        else:
            return "Жаль, но из этого треугольник не сделать."


# Задание 3
class KgToPounds:
    def __init__(self, kg):
        self.__kg = kg

    def to_pounds(self):
        return self.__kg * 2.20462

    def set_kg(self, value):
        if isinstance(value, (int, float)):
            self.__kg = value
        else:
            return "Нужно вводить только числа"

    def get_kg(self):
        return self.__kg

# Задание 5
class Ractangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def str(self):
        return f"Прямоугольник с шириной {self.width} и высотой {self.height}"

    def get_area(self):
        return (self.width * self.height) // 2

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    @property
    def is_square(self):
        return self.width == self.height

# Задание 6
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def str(self):
        return f"“Имя:{self.name}, Возраст: {self.age}, Пол: {self.gender}"

    def get_name(self):
        return self.name\

    @property
    def n_name(self):
        return self.n_name

    @n_name.setter
    def n_name(self, new_name):
        self.name = new_name

    @staticmethod
    def is_adult(age):
        if age >= 18:
            return True
        else:
            return False

    @classmethod
    def create_from_string(cls, s):
        name, age, gender = s.split("-")
        return cls(name, int(age), gender)


