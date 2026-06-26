# Задание 7

numbers = [3, 6, 2, 9, 5, 12, 7, 15, 4]

def sum_even_between(nums, start, end):
    total = 0
    for num in nums[start:end+1]:
        if num % 2 == 0:
            total += num
    return total


print(sum_even_between(numbers, 2, 7))