# Задание 1

numbers = [10, -5, 3, 0, 8, -2, 7]

def new_spis(numbers):
    new_numbers = []
    for number in numbers:
        if number > 0:
            new_numbers.append(number * 3)

    return new_numbers


print(new_spis(numbers))