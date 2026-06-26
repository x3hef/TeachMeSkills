# Задание 5

nums = [1,100,3,5,5,3,7,8,9]
n = nums[0]
for i in range(len(nums)):
    if nums[i] >= n:
        n = nums[i]



print(n)