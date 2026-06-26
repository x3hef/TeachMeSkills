# Задание 6

def value(x):
    if x % 1 == x % x:
        print(f"{x}- простое число")
    else:
        print(x - "Непростое число")


x = int(input())
value(x)