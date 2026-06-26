users = [
    {"username": "admin", "password": "12346789", "email": "admin@mail.ru"},
    {"username": "user", "password": "12345", "email": "user@gmail.com"},
]


def get_user_by_username(username) -> dict:
    for user in users:
        if user["username"] == username:
            return user

    raise ValueError(f"User with username {username} not found")
    # return None



def main():
    username = input("Username: ")
    password = input("Password: ")

    try:
        user = get_user_by_username(username)
    except ValueError as exc:
        print(exc)
        return

    if user["password"] != password:
        print("Incorrect password")
        return

    print(f"Welcome {username}!")


main()