
number = 1 / 3 * 100

text0 = "Скидка: %s%%" % round(number, 2)
print(text0)


round_number = round(number, 2)
text = "Скидка: " + str(round_number) + "%"
print(text)


text2 = "Скидка: {1}% -> {0}%".format(round_number, number)
print(text2)


number = 1 / 3 * 100
text3 = f"Скидка: {round(1 / 3 * 100, 2)}%"
print(text3)


text4 = "Скидка: {1}% -> {0:.2f}%".format(number, number)
print(text4)


text5 = f"Скидка: {number:.2f}%"
print(text5)


p = 4
text6 = f"Скидка: {number:.{p}f}%"
print(text6)
