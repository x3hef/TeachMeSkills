# Задание 3

nums = [1,2,2,1,3,4,3,4,5,2,1]
k = 0
nums_new = []

for i in range(len(nums)):
    if i not in nums:
        nums_new.append(nums[i])
    else:
        k += 1


print(nums_new)
print(k)

def removeDuplicates(nums):
    if not nums:
        return 0

    k = 1  # первый элемент уже уникальный

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1

    return k