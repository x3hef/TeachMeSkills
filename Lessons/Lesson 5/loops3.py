from string import ascii_letters

text = '1, 2, "text", 34.12, "Привет", None'


numbers = ""

for letter in text:
    if letter in ascii_letters:
        numbers += letter

    if letter in "[]":
        print("Ошибка в тексте")
        break

else:
    # Блок else в циклах выполняется, когда цикл завершился без break.
    print("Обработали текст без ошибок")

print(numbers)