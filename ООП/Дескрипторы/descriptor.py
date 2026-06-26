# Дескрипторы

# class Point3D:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     @classmethod
#     def verify_cor(cls, cords):
#         if type(cords) != int:
#             raise TypeError
#
#     @property
#     def x(self):
#         return self.x
#
#     @x.setter
#     def x(self, cords):
#         self.verify_cor(cords)
#         self.x = cords
#
#     @property
#     def y(self):
#         return self.y
#
#     @y.setter
#     def y(self, cords):
#         self.verify_cor(cords)
#         self.y = cords
#
#     @property
#     def z(self):
#         return self.z
#
#     @z.setter
#     def z(self, cords):
#         self.verify_cor(cords)
#         self.z = cords

class Point3D:
    x = Integer3D()
    y = Integer3D()
    z = Integer3D()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class Integer3D:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print(f"__set__: {self.name} = {value}")
        instance.__dict__[self.name] = value