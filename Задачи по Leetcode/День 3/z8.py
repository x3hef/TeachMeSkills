# Задание 8

nams = [1,1,1,2,3,2,3,4,1,4,5,6]
num_new = []

for i in range(0,len(nams)):
    if nams[i] not in num_new:
        num_new.append(nams[i])

print(num_new, len(num_new))