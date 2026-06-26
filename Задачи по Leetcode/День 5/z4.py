# Задание 4

numbers = [12, 5, 8, 7, 21, 14, 3, 10]
new_numbers = []
total = 0
for i in numbers:
    if i > 10:
        new_numbers.append(i**2)
total = sum(new_numbers)
print(total)
