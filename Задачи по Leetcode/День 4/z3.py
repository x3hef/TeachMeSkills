# Задание 3
from mypy.server import target

nums = [2,7,11,15]

def twoSum(nums):
    target = 9
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return f"{[i, j]}"


print(twoSum(nums))
