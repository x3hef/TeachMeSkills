# Задание 2

n = int(input("Введите  число от 1 до N:"))
count = 1

for i in range(1, n + 1):
    count *= i

print(count)