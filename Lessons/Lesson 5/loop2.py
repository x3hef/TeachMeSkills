list1 = [1, 2, "text", 34.12, "Привет", None, [], [12]]

strings = []
others = []
lists = []


for element in list1:

    if element is None:
        # print("В списке был обнаружен None. Прекращаем работу!")
        continue

    if isinstance(element, str):
        # Если элемент списка является экземпляром класса (типом) `str`.
        strings.append(element)
    elif isinstance(element, list):
        lists.append(element)
    else:
        # Иначе это числа.
        others.append(element)

print(strings)
print(others)
print(lists)