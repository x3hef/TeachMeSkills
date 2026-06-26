# Классы и объекты в Python

class Point:
    circle2 = None
    color = "red"
    circle = 2


Point.color = "black"

print(Point.color)
print(Point.circle)

print(Point.__dict__)

a = Point()
print(a.color)
print(a.circle)

b = Point()
print(b.color)
print(b.circle)

print(id(b))
print(id(a))

print(a.__dict__)
print(b.__dict__)

setattr(Point, "color", "green")
setattr(Point, "circle2", 6)

print(Point.color)
print(Point.circle)
print(Point.circle2)

print(getattr(Point, "a", False))
print(getattr(Point, "circle", False))

del Point.circle
print(getattr(Point, "circle", False))

print(hasattr(Point, "circle2"))
print(getattr(Point, "circle2", False))

delattr(Point, "circle2")
print(getattr(Point, "circle2", False))