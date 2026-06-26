# Примеры работы с циклом for


n = int(input("Введите натуральное число не больше 100: "))

if n < 1 or n > 100:
    print("No")
else:
    p = 1
    for i in range(1, n + 1):
         p *= i

    print(f"факториал числа {n}! = {p}")

for i in range(1, 7):
    print("*" * i)


words = ["a", "b", "c"]

s = ""

for word in words:
    s += " " + word

print(s)

digs = [1, 2,55,-55,32]

for i in range(len(digs)):
    if 10 <= abs(digs[i]) <= 99:
        digs[i] = 0

print(digs)

# индекс, значение = enumerate(объект)


for i ,d in enumerate(digs):
    if 10 <= abs(d) <= 99:
        d =  0

print(digs)

