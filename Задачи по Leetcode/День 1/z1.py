# Задание 1

n = int(input("Введите число: "))

for i in range(1,n+1):
    if i % 3 == 0 and i % 2 !=0:
        print(i)

# Задание 2

total = 0

for i in range(1,n+1):
    if i % 2 == 0 or i % 3 ==0:
        total += i

print(total)

# Задание 4

c = [1, 2, 3, 4, 5, 6, 7, 8]

c_new = []
for i in range(len(c)):
    if c[i] > 3 and c[i] % 2 == 0:
        c_new.append(c[i])
print(c_new)

