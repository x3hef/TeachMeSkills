b = [1,2,3,4,5,6]

flFind = False
i = 0

while i < len(b):
    flFind = b[i] % 2 == 0
    if flFind:
        break

    i += 1

s = 0
d = 1

while d != 0:
    d = int(input("Введите целое число "))
    if d % 2 == 0:
        continue

    s += d
    print("s =" + str(s))

while d != 0:
    d = int(input("Введите целое число "))
    if d % 2 == 0:
        continue
else: # - необязательный
    pass