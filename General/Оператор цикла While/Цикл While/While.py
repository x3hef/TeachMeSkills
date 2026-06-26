# While - делаем цикл пока оно True!

# While <условие>: - заголовок цикла
    # оператор 1
    # оператор 2 - тело цикла
    # ...
    # Оператор N


n = 1000
s = 0
i = 1

while i <= n:
    s += i
    i += 1 # - итерация цикла

while i <= n and i <= 50:
    s += i
    i += 1 # - итерация цикла


while i <= n and i <= 50:
    s += i
    i += 2 # - итерация цикла

while i < 10:
    print(i)

while i < 10:
    print(i)
    i += 1

# убывающий цикл

N = -10
i =-1

while i >= N:
    print(i)
    i -= 1

pass_true = "pass"
ps = ""

while ps != pass_true:
    ps = input("Введите пароль")

print("Вход в систему")


N2 = 20
i = 1
while i <= N2:
    if i % 3 == 0:
        print(i)

    i += 1
    
