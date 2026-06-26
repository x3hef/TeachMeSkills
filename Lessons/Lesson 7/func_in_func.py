from typing import Callable


def get_valid_users(users: list[dict], validator: Callable[[dict], dict]) -> list[dict]:
    result: list[dict] = []

    for user in users:
        print("Validating user: ", user)
        valid_user = validator(user)
        print("Valid user: ", valid_user)
        result.append(valid_user)
        print()

    return result


def user_validator(user: dict) -> dict:
    if not user.get("email"):
        user["email"] = ""

    user["username"] = user["username"].lower()
    return user


def create_validator(valid_email=True, valid_username=False) -> Callable[[dict], dict]:

    def inner_validator(user: dict) -> dict:
        if valid_email and not user.get("email"):
            user["email"] = ""
        if valid_username:
            user["username"] = user["username"].lower()
        return user

    return inner_validator


users = [
    {
        "username": "user2",
    },
    {
        "username": "user1",
        "email": "user1@gmail.com",
    },
    {
        "username": "User3",
        "email": "user3@yandex.com",
    },
]

validator = create_validator(valid_email=True, valid_username=True)

valid_users = get_valid_users(users, validator)