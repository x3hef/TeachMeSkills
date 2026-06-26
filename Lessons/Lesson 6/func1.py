number = 123  # int(input("Enter a number 1: "))
number2 = -23  # int(input("Enter a number 2: "))
number3 = 0  # int(input("Enter a number 3: "))

input_list = [number, number2, number3]

results = []  # [True, False, None]

for n in input_list:
    if n > 0:
        results.append(True)
    elif n < 0:
        results.append(False)
    else:
        results.append(None)


print("Сумма чисел: ", sum(input_list))

number = 123  # int(input("Enter a number 1: "))
number2 = -23  # int(input("Enter a number 2: "))
number3 = 0  # int(input("Enter a number 3: "))

input_list = [number, number2, number3]


for n in input_list:
    if n > 0:
        results.append(True)
    elif n < 0:
        results.append(False)
    else:
        results.append(None)


mult = 1
for n in input_list:
    mult = mult * n

print("Произведение чисел: ", mult)


print(results)