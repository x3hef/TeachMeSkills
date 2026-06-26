# __slots__

import timeit

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point2:

    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y


def make_cl1():
    s = Point2(1, 2)
    s.x = 3
    del s.x

def make_cl2():
    s = Point2(1, 2)
    s.x = 3
    del s.x
