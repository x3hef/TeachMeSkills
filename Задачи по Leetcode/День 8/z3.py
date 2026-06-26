# Задание 3

n = int(input("Введите число от 1 до N"))

if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
if n % 3 == 0:
    print("FIZZ")
if n % 5 == 0:
    print("BUZZ")
else:
    print(n)


