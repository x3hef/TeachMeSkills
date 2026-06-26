# if - условный оператор(оператор ветвления)

# If <условие>:
# оператор 1
# оператор 2
# ...
# Оператор N

x = -4

if x < 0:
    x = -x
print(x)

x = int(input())

if -4 <= x <= 10:
    print(x)

if x:
    print(x)

x = [3, 4, 5, 3, 2]

if 2 in x:
    print("if")
else:
    print("else")

x = int(input())

if x < 0:
    print("x < 0")
else:
    print("x >= 0")

x = int(input())

if x % 2 == 0:
    print("even")
else:
    print("odd")

# максимальное из трех чисел

a = 3
b = 4
c = 6

