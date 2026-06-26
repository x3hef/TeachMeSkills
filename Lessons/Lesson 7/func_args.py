import random
import string


def user_password_generator(max_length: int = 8):
    passwd = ""
    for i in range(max_length):
        passwd += random.choice(string.ascii_letters + string.digits)

    return passwd


def create_user(username: str, email: str, *args, **kwargs) -> dict:

    user = {
        'username': username,
        'email': email,
        'password': user_password_generator(*args, **kwargs),
    }

    return user


u1 = create_user(
    'user1',
    'user1@mail.com',
    max_length=12,
)

print(u1)