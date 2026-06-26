# оператор return

def get_sqrt(x):
    res = None if x < 0 else x ** 0.5
    return res

print(get_sqrt(5))