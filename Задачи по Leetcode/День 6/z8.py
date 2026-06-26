# Задание 8

def removeDuplicates(nums):
    new_nums = []
    count = 0
    for num in nums:
        if num not in new_nums:
            new_nums.append(num)
            count += 1

    return f"{new_nums} ---> {count}"
nums = [0,0,1,1,1,2,2,3,3,4]

print(removeDuplicates(nums))