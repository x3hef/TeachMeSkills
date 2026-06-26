
list_users = ["user1", "user2", "user3"]
list_users2 = list(list_users)

print("List users:", list_users)
print("List users2:", list_users2)

list_users.append("user4")

print("List users:", list_users)
print("List users2:", list_users2)


# ====================================================


text_0 = "text_0"
text_1 = text_0

print("Text 0:", text_0)
print("Text 1:", text_1)

text_1 += "1"

print("Text 0:", text_0)
print("Text 1:", text_1)
