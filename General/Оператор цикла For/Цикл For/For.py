# Оператор цикла for

# break - досрочное завершение цикла
# continue - пропуск одной итерации цикла
# else - выполнение блока операторов после завершения цикла

# For <переменная> in <итерируемый объект>: - заголовок
# оператор 1
# оператор 2 - тело цикла
# ...
# Оператор N

d = [1, 2, 3, 4, 5]

for i in d:
    print(i)

p = 0
for i in d:
    p += i
    print(p)

# функция range() - генерирует последовательность
# range(start, stop, step)

range(5)
list(range(5))
print(list(range(5)))

for i in range(5):
    print(i)

S = 0

for i in range(2, 1001):
    S += 1/i

print(S)

