list1 = [1, 2, "text", 34.12, "Привет", [], [12]]

strings = []
numbers = []
lists = []

index = 0
while index < len(list1):

    if isinstance(list1[index], str):
        # Если элемент списка является экземпляром класса (типом) `str`.
        strings.append(list1[index])
    elif isinstance(list1[index], list):
        lists.append(list1[index])
    else:
        # Иначе это числа.
        numbers.append(list1[index])

    index += 1


print(strings)
print(numbers)
print(lists)


# ==============================================================================

list1 = [1, 2, "text", 34.12, "Привет", None, [], [12]]

strings = []
others = []
lists = []

index = len(list1)
while index >= 0:
    index -= 1
    print(index)

    if list1[index] is None:
        continue  # Переходим к проверке условия цикла.

    if isinstance(list1[index], str):
        # Если элемент списка является экземпляром класса (типом) `str`.
        strings.append(list1[index])
    elif isinstance(list1[index], list):
        lists.append(list1[index])
    else:
        # Иначе это числа.
        others.append(list1[index])

print(strings)
print(others)
print(lists)



# ==============================================================================

list1 = [1, 2, "text", 34.12, "Привет", None, [], [12]]

strings = []
others = []
lists = []

index = len(list1)
while index >= 0:
    index -= 1
    print(index)

    if list1[index] is None:
        print("В списке был обнаружен None. Прекращаем работу!")
        break

    if isinstance(list1[index], str):
        # Если элемент списка является экземпляром класса (типом) `str`.
        strings.append(list1[index])
    elif isinstance(list1[index], list):
        lists.append(list1[index])
    else:
        # Иначе это числа.
        others.append(list1[index])

print(strings)
print(others)
print(lists)