# property

class Circle:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

circle = Circle(5)
print(circle.radius)