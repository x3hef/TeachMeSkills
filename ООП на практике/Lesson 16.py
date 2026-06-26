# Специальные методы сравнения

# Магические методы сравнение

# __eq__ = "=="
# __ne__ = "!="
# __lt__ = "<"
# __le__ = "<=>
# __qt__ = ">"
# __qe__ = ">="

class Rectangle:
    def __init__(self, a, b):
        self.x = a
        self.y = b

    @property
    def area(self):
        return self.x * self.y

    def __eq___(self,other):
        print("call")
        if isinstance(other,Rectangle):
            return self.x == other.x and self.y == other.y
        return False
    def __lt__(self,other):
        print("call")
        if isinstance(other,Rectangle):
            return self.area < other.area
        elif isinstance(other, (int, float)):
            return self.area < other
        else:
            return False

q = Rectangle(2, 3)
v = Rectangle(4, 5)
print(q < v)