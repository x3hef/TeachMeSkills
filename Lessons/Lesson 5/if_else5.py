users1 = ["", "user2", "user3", 1, None]
users2 = []
users3 = ["user2", "user3"]

if users2 and users2[0]:
    print("Первый элемент списка не пустой")

x = "None"

if x not in users1:
    print(f"В списке 1 нет `{x}`.")


text = "This chapter explains the meaning of the elements of expressions in PyTHon."
word = "Python"

if word.lower() in text.lower():
    print("В тексте есть упоминание Python")


# ====================================================================================

users = ["user1", "user2", "user3"]
admin_users = users

if users is admin_users:
    print("Список пользователей и администраторов один и тот же объект!")

if users == admin_users:
    print("Список пользователей и администраторов равны")


# ====================================================================================

users = ["user1", "user2", "", None, ""]
index = 2

#  users          and  len(users) > index     and  not users[index]
#  bool(users)    and  5 > 2                  and  not users[2]
#  bool([...]])   and  True                   and  not ""
#  True           and  True                   and  not bool("")
#  True           and  True                   adn  not False
#  True           and  True                   and  True
#  True

print("Проверка без использования None")
if users and len(users) > index and not users[index]:
    print(f"Отсутствует {index + 1}й элемент в списке `{users[index]}`")

# ====================================================================================

users = ["user1", "user2", "", None, ""]
index = 3

#  users          and  len(users) > index     and  not users[index]
#  bool(users)    and  5 > 2                  and  not users[2]
#  bool([...]])   and  True                   and  not ""
#  True           and  True                   and  not bool("")
#  True           and  True                   and  not False
#  True           and  True                   and  True
#  True

print("Проверка с использованием None")
if users and len(users) > index and users[index] is None:
    print(f"Отсутствует {index + 1}й элемент в списке `{users[index]}`")