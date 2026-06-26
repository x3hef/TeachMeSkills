# Задание 8

def maxEven(nums):
    max_elem = None
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            max_elem >= nums[i]
            max_elem = nums[i]

    return max_elem


print(maxEven([1, 3, 5]))