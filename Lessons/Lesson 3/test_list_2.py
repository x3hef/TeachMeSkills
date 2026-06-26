# Индексы         0        1        2
users_names = ["user1", "user2", "user3"]
users_emails = ["user1@mail.com", "", "user3@mail.com"]


# Индексы
users = [
    ["user1", "user1@mail.com"],  # users[0]
    ["user2", "user2@mail.com"],  # users[1]
    ["user3", "user3@mail.com"],  # users[2]
]

first_user_email = users[0][1]

print(users[0])

# users[0][1]  ->  ["user1", "user1@mail.com"][1]  ->  "user1@mail.com"

# users[2][0]  ->  ["user3", "user3@mail.com"][3]    !!!!!!!!!!!!!ERROR

print(first_user_email)