# Магический метод New

class Point:

    def __new__(cls, *args, **kwargs): # cls - сслылка на текуший экземпляр класса
        print("вызов метода __new__" + str(cls))
        return super().__new__(cls)

    def __init__(self, x=0, y=0):
        print("Вызов метода __init__")
        self.x = x
        self.y = y

pt = Point(1,2)