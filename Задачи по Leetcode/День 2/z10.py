# Задание 10

def negative(num):
    for i in range(len(num)):
        if num[i] < 0:
            num[i] = 0
    return num

num = [1,2,3,4,5,-1,-2]
print(negative(num))