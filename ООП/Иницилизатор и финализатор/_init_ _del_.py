# Инициализатор и финализатор

# __имя магического метода__

# __init__(self) - Инициализатор объекта
# __dell__(self( - финализатор объекта

class Point:
    def __init__(self, x=0, y=0):
        print("Вызов метода __init__")
        self.x = x
        self.y = y

    def __del__(self):
        print("финализатор")
    
    def set_coords(self):
        pass
    def ger_coords(self):
        return self.x, self.y


pt = Point(10,30) #Вызов метода __init__
print(pt.__dict__) # {'x': 10, 'y': 30}



