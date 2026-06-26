# Алгоритм Евклида
# НОД - наибольший общий делитель

def get_nod(a,d):
    """Вычисляется НОД для натуральных чисел a и b
        по алгоритму Евклида
        :param a: первое натуральное число
        :param d: второе натуральное число
        :return НОД"""
    while a != d:
        if a > d:
            a -= d
        else:
            d -= a

    return a

def test_nod(func):
    """Test 1"""
    a = 28
    b = 35
    res = func(a, b)
    if res == 7:
        print("Yes")
    else:
        print("No")



res = get_nod(18,24)
print(res)


