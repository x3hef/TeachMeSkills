# Декораторы функций с параметрами
import math


def func_decorator(func):
    def wrapper(*args, **kwargs):
        dx = 0.0001
        res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
        return res
    return wrapper

@func_decorator
def sin_df(x):
    return math.sin(x)