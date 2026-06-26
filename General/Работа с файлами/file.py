# Работа с файлами

file = open("text.txt", "w", encoding="utf-8")

file.write("Привет Мир\n")
file.write("!!!")

file = open("text.txt", "r", encoding="utf-8")

print(file.read())

for line in file:
    print(line)

file.close()
