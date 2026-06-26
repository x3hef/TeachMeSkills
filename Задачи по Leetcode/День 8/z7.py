# Задание 7

d = "dfjghdfjghdfjhgdf"
d2 = {}

for i in d:
    if i not in d2:
        d2.update({i:1})
    if i in d2:
        d2.update({i:+1})


print(d2)