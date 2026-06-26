# Метода классов

# class
    # свойства(данные)
    # методы(действия)

class Point:
    color = "red"
    circle =  4

    def set_coords(self, x, y): # - метод класса 
        self.x = x
        self.y = y
        print("Вызов метода" + str(self))


pt = Point() # - экземпляр класса
pt.set_coords(2,3) # - Вызов метода<__main__.Point object at 0x0000020A17A98D70>
print(pt.__dict__)
# pt.set_coords() - self ссылка на экземпляр класса


