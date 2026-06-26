u4 = "user4"

users_names = {"user1", "user1", "user1", "user1", "user2", "user3", u4, 1}

print(type(users_names))
print(users_names)

# =========================================================

# Нельзя в множестве выбрать по индексу ❗️❗️❗️
# print(users_names[3])

set_length = len(users_names)

print("Длина множества:", set_length)

users_names.add(u4)
users_names.add(u4)
users_names.add(u4)
users_names.add(u4)

print("Длина множества:", set_length)