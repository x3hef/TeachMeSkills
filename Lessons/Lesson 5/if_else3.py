user_input = input("Введите число: ")

if user_input.isdigit():
    n = int(user_input)

    if n > 0:
        print("Число положительное")
    elif n < 0:
        print("Число отрицательное")
    else:
        print("Число равно нулю")

# ==================================================


user_input = input("Введите число: ")

if user_input.isdigit():
    n = int(user_input)

    if n > 0:
        print("Число положительное")
    else:
        if n == -6:
            print("Число -6")
        else:
            if n < 0:
                print("Отрицательное")
            else:
                print("Число равно нулю")

# ==================================================

user_input = input("Введите число: ")

if user_input.isdigit():
    n = int(user_input)

    if n > 0:
        print("Число положительное")
    elif n == -6:
        print("Число -6")
    elif n < 0:
        print("Отрицательное")
    else:
        print("Число равно нулю")