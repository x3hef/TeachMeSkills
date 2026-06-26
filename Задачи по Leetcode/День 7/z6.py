# Задание 6

nums = [1,2,2,2,3,3,4,4,5,5]

def singleNumber(nums):
    result = 0
    for i in nums:
        result ^= i
        return result

print(singleNumber(nums))

