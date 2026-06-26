#  Вычисляемые property

class Square:
    def __init__(self, s):
        self.__side = s
        self.__area = None

    @property
    def side(self):
        return self.__area
    @side.setter
    def side(self, value):
        self.__side = value
        self.__area = None


    @property
    def area(self):
        if self.__area is None:
            print("call area")
            self.__area = self.side ** 2
        return self.__area


c = Square(5)
print(c.area)
print(c.side)
