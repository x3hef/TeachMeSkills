def get_user_detail(user: dict, use_email: bool = True, use_address: bool = False) -> str:
    """
    Возвращает полное имя пользователя.
    :param user: Словарь
    :param use_email: Добавлять ли email.
    :param use_address: Добавлять ли address.
    :return: Строку.
    """
    res = f"{user['first_name']} {user['last_name']}"
    if use_email:
        res += f" {user['email']}"
    if use_address:
        res += f" Address: {user['address']["city"]}"
    return res


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

full_name = get_user_detail(user_1)

print(full_name)