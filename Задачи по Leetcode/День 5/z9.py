# Задание 9

numbers = [4, 2, 5, 2, 3, 4, 1, 5]
new_list = []

for i in numbers:
    if i not in new_list:
        new_list.append(i)


print(new_list)