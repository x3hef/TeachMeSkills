# Обработка исключений

try:
    x = int(input())
    x += 4
    print(x)
except ValueError:
    print("Введите число")
finally:
    print("finally")