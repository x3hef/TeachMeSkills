# Магические метод bool

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __bool__(self):
        return self.x > 0 or self.y > 0

a = Point(1, 2)
print(a.__bool__())