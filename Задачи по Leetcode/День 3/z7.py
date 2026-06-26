# Задание 7

nums1 = [1,2,3,4,5,6,7,8,9]
nums2 = [2,3,4,6,7,8,9]
num3 = []
for num in nums1:
    for num2 in nums2:
        if num == num2:
            num3.append(num)

print(num3)



