# Задание 1
# Название: Two Sum
# Ссылка: LeetCode Two Sum
#
# Описание:
# Дан массив чисел nums и целое число target. Нужно найти два числа в массиве,
# сумма которых равна target, и вернуть их индексы.
#
# Можно вернуть индексы в любом порядке.
# Предполагается, что ровно одно решение существует.
# Нельзя использовать один и тот же элемент дважды.

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [nums[i], nums[j]]