# Функция генератора

def get_list():
    for x in range (10):
        yield x


a = get_list()
print(next(a)) # - <generator object get_list at 0x0000020AB8F98EE0>

for x in a:
    print(x)
def get_list2():
    for x in range (1,10):
        a = range(1,10)
        yield sum(a) / len(a)

print(list(get_list2()))

