a = 1
b = 2

res = a if a > b else b

print(res)

res = a + 2 if a > b else b + 3

print(res)

res = abs(a) if a > b else abs(b)

print(res)

s  = "Python"
t = 'upper'

res = s.upper() if t == 'upper' else s
print(res)

