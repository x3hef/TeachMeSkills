# Вложенные циклы

for i in range(1, 4):
    for j in range(1, 6):
        print(f" i = {i}, j = {j}", end="")
    print() # - переход на новую строку

# Вывод:
        # i = 1, j = 1 i = 1, j = 2 i = 1, j = 3 i = 1, j = 4 i = 1, j = 5
        # i = 2, j = 1 i = 2, j = 2 i = 2, j = 3 i = 2, j = 4 i = 2, j = 5
        # i = 3, j = 1 i = 3, j = 2 i = 3, j = 3 i = 3, j = 4 i = 3, j = 5

a = [[1,2,3],[4,5,6],[7,8,9]]

for row in a:
    for x in row:
        print(x, end=" ")
    print()

