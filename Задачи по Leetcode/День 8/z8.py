# Задание 8

x = [1,3,4,5,6,7]
count_1 = 0
count_2 = 0

for i in x:
    if i % 2 == 0:
        count_1 += i
    if i % 2 != 0:
        count_2 += i


print(count_1, count_2)
