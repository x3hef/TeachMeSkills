# Функция zip
# zip(iter1 [,iter2 [,iter3 ...])


a = [1, 2, 3]
b = [4, 5, 6, 3]

z = zip(a, b)
print(list(z)) # - [(1, 4), (2, 5), (3, 6)] - только один раз

for i in z:
    print(i)

