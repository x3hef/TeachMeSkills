# Задание 6

def secondMax(nums):
    max_num = float('-inf')
    second_max = float('-inf')

    for num in nums:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif num > second_max and num != max_num:
            second_max = num

    return second_max


print(secondMax([10, 5, 8, 20]))