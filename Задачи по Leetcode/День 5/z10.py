# Задание 10


numbers = [3, 6, 2, 9, 6, 3, 6, 2]
count_dict = {}

for num in numbers:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

print(count_dict)