# Задание 4
# С сайта LeetCode
# Задача: Contains Duplicate
#
# Дан список чисел nums. Нужно вернуть True,
# если в списке есть хотя бы один повторяющийся элемент, иначе False.

nums = [1,2,3,4,5,6,7,8,9,1]
nums_new = set(nums)
def solution(nums, nums_new):
    if len(nums_new) == len(nums):
        return False
    else:
        return True

print(solution(nums, nums_new))

def containsDuplicate(nums):
    return len(set(nums)) != len(nums)

nums = [1,2,3,4,5,6,7,8,9,1]
print(containsDuplicate(nums))