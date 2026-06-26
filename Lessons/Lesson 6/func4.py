

def get_verbose_name(user: dict) -> str:
    """
    Возвращает полное имя пользователя.
    :param user: Словарь с ключами `first_name` и `last_name`.
    :return: Строку.
    """
    return f"{user['first_name'].title()} {user['last_name'].title()}"


def is_valid_email(email: str) -> bool:
    """Проверяет правильный ли email"""
    return "@" in email and "." in email and len(email) <= 2048


def get_full_address(address: dict) -> str:
    text = ""
    for key, value in address.items():
        text += f"{key}: {value} "
    return text


user_1 = {
    "username": "ivan",
    "first_name": "Ivan",
    "last_name": "Ivanov",
    "email": "ivan@mail.com",
    "age": 25,
    "address": {
        "city": "New York",
        "street": "1st"
    }
}

full_name = get_verbose_name(user_1)

if not is_valid_email(user_1["email"]):
    print("Укажите верный EMAIL!")

print(full_name.lower())


user_address = get_full_address(user_1["address"])

print(user_address)