# Генератора списков(List comprehension)
# |<способ формирования значения> for <счётчик> in <итерируемый объект>

a = [(i, j)
     for i in range(10)
     for j in range(10)
     ]

print(a)

a = [(i, j)
     for i in range(10) if i % 3 == 0
     for j in range(10) if j % 3 == 0
     ]

print(a)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

a = [x for row in matrix for x in row]  # type: ignore[misc]
print(a)

M, N = 3, 4

matrix = [[a for a in range(M)] for b in range(N)]
print(matrix)

A = [[0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]]

a = [[x ** 2 for x in row] for row in matrix]  # type: ignore[misc]
print(a)
