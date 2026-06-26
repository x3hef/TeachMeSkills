# Задание 10

numbers = [3, 6, 2, 9, 5, 12, 7, 15, 4]

def nums(numbers):
    number_sum = 0
    for number in numbers:
        if number % 3 == 0 and number % 2 != 0:
            number_sum += number * 3

    return number_sum

