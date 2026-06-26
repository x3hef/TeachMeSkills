# Полиморфизм

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_rect_area(self):
        return self.width * self.height


class Square:
    def __init__(self, width):
        self.width = width

    def get_rect_area(self):
        return self.width ** 2
