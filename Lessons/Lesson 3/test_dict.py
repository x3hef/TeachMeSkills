user1 = {
    "username": "user1",
    "email": "user1@mail.com",
}

print(user1["username"])
print(user1["email"])

user1["email"] = "new1@mail.com"

print(user1["email"])

user1["password"] = "qwerty!@#"


user1.pop("password")  # Удалили пароль

print(user1.get("password"))  # Вернёт `None`.

print(user1.get("password", '*'))  # Вернёт `*`.