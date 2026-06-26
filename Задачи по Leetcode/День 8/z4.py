from os import remove

t = "hello"
vowels = "aeiou"

for i in t:
    if i in vowels:
        remove(t[i])