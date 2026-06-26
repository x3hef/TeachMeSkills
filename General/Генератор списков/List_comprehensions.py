# Генератор списков

a = [x **2 for x in range(10)] # - [<способ формирования значения> for <переменная> in <итерируемый объект>
print(a)

b = [1 for x in range(10)]
print(b)

b = [1] * 10
print(b)

a = [x % 4 for x in range(10)]
print(a)

a = [x % 2 for x in range(10)]
print(a)

a = [0.5 * x  + 1 for x in range(10)]  # type: ignore[misc]
print(a)

a = [int(d) for d in range(10)]
print(a)

a = [ord(d) for d in "python"]
print(a)