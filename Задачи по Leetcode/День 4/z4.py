# Задание 4

nums = [1,1,2,3,3,4,4,1,2]

def contains(nums):
    new_list = []
    for i in nums:
        if i not in new_list:
            new_list.append(i)

    return new_list

print(contains(nums))

nums = [1,1,1,2,2,3,3,4,4,5,5]

if len(nums) != len(set(nums)):
    print(True)
else:
    print(False)
print(contains(nums))

