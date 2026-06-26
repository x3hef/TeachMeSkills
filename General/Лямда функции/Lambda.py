# Лямбда функция - анонимные функции

s = lambda a, b: a + b
print(s(1,2))

a = [1,2,lambda: print(s)]
print(a)

lst = [4,6,7,-5]

def get_filter(a, filter=None):
    if filter is None:
        return a
    res = []
    for i in a:
        if filter(i):
            res.append(i)

    return res

r = get_filter(lst, lambda i: i % 2 == 0)
print(r)

a = lambda x, y: x * y

a = a(3,4)
print(a)


