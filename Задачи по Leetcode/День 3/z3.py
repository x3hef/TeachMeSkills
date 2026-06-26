# Задание 3

def sortedNumbers(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2

    return sorted(nums, reverse=False)

print(sortedNumbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))