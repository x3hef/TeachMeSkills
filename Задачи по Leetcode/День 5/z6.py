# Задание 6

words = ["apple", "banana", "apple", "orange", "banana", "kiwi"]
unik_words = []
for word in words:
    if word not in unik_words:
        unik_words.append(word)

print(unik_words)