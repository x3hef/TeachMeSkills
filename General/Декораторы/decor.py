# Декораторы функций

import webbrowser

def func_decorator(func):
    def wrapper(*args, **kwargs):
        print("1")
        func(*args, **kwargs)
        print("2")

    return wrapper

def some_func():
    print("3")

some_func = func_decorator(some_func)
some_func()

def validator(func):
    def wrapper(url): # - обертка
        if "." in url:
            func(url)
        else:
            print("Неверный url!")
    return wrapper


@validator
def open_url(url):
    webbrowser.open(url)

open_url("https://wwwgooglecom")

# Декораторы - это функция, которая позволяет обернуть другую функцию
# для расширения её функциональности без изменения её исходного кода
