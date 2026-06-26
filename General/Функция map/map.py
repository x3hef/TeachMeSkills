# Функция map

b = map(int, ["1", "2", "3", "4", "5", "6", "7", "8", "9"])

print(next(b))
print(next(b))

d = (int(x) for x in ["1", "2", "3", "4", "5", "6", "7", "8", "9"])

c = list(d)
print(c)