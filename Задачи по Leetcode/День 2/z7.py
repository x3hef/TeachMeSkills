# Задание 7
n = [1, -2, 3, 0, 5]


def polnumbers(n):

    sum = 0
    for num in range(len(n)):
        if n[num] > 0:
            sum += 1
    return sum


print(polnumbers(n))