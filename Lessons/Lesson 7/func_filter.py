users = [
    {
        "username": "user2",
        "email": "",
    },
    {
        "username": "user1",
        "email": "user1@gmail.com",
    },
    {
        "username": "user3",
        "email": "user3@yandex.com",
    },
]

print(users)


# Пользователи только с email.

valid_users: list[dict] = []

for user in users:
    if user.get("email"):
        valid_users.append(user)


# =======================================


def validator(user: dict) -> bool:
    return bool(user.get("email"))

# Аналог
# lambda user: bool(user.get("email"))
valid_users_with_email = filter(lambda user: bool(user.get("email")), users)

print(valid_users_with_email)


# lambda user: user["email"].endswith("@gmail.com")
gmail_users = list(filter(lambda user: user["email"].endswith("@gmail.com"), valid_users_with_email))

print(gmail_users)