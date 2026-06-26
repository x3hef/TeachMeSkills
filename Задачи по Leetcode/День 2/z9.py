# Задание 9

def countNumbers(nums):
    x = 2
    total = 0
    for num in range(len(nums)):
        if x == nums[num]:
             total += 1

    return total

print(countNumbers(nums = [1,2,2,3,2,3]))