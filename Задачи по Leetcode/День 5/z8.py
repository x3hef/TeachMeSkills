# Задание 8

numbers = [1, 2, 3, 4, 5, 6]
new_list = []
for i in numbers:
    if i % 2 == 0:
        new_list.append(i*2)

print(new_list)