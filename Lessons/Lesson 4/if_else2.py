users = []

# !!!!!!!!!! КАК НЕ НАДО ПИСАТЬ !!!!!!!!!!!
#  ` == False`
#  ` == True`

if bool(users) != True:
    user_input = input("Введите пользователя: ")
    users.append(user_input.strip())

# bool(users) != True
#    bool([]) != True
#       False != True
#            True

print(users)


# Ну, так можно писать...

# not bool(users)
# not bool([])
# not False
# True

if not bool(users):
    user_input = input("Введите пользователя: ")
    users.append(user_input.strip())


# ! ПИШЕМ ТАК !

# not users
# not bool(users)
# not bool([])
# not False
# True

if not users:
    user_input = input("Введите пользователя: ")
    users.append(user_input.strip())