# Функция filter()

# filter(func, *iterables) - фильтрация элементов итерированного объекта

a = [1,2,3,4,5,6,7,8,9,10]

b = filter(lambda x: x % 2 == 0, a)
print(list(b))

