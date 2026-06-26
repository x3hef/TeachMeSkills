# Задание 1
from sqlalchemy.sql.functions import count

n = int(input("Введите число: "))

for i in range(1, n + 1):
    if i % 4 == 0 or i % 6 ==0:
        print(i)

# Задание 2

n = input("Введите строку")
glas = 'aeiouy'
count = 0
for i in glas:
    if i in n:
        count += 1

print(count)

# Задание 3

v = input("Введите строку: ")

v = v.lower()

if v == v[::-1]:
    print("YES")
else:
    print("NO")


l = [1, 2, 3, 4, 5, 6, 7, 8]
l_new =[]
for i in l:
    if i % 2 == 0:
        l_new.append(i * 2)
    else:
        l_new.append(i)

print(l_new)

