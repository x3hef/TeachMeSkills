# Рекурсивные функции


def rcs3(x):
    print(x)

def rcs2(x):
    print(x)
    rcs3(x - 1)
    print(x)

def rcs1(x):
    print(x)
    rcs2(x - 1)
    print(x)

rcs1(3)

