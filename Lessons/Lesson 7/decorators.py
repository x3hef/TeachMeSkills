import time
import random
import string


def timer(func):

    def wrapper(*args, **kwargs):
        print(f"Начало работы декоратора для функции {func.__name__}")
        start_time = time.perf_counter()

        res = func(*args, **kwargs)

        end_time = time.perf_counter()

        print(f'Function: {func.__name__} {args}, {kwargs} | Time taken: {end_time - start_time} seconds')

        print(f"Конец работы декоратора для функции {func.__name__}")
        return res

    return wrapper


@timer
def user_password_generator(max_length: int = 12) -> str:
    passwd = ""
    for i in range(max_length):
        passwd += random.choice(string.ascii_letters + string.digits)

    return passwd


@timer
def create_user(username: str, email: str) -> dict:
    user = {
        'username': username,
        'email': email,
        'password': user_password_generator(),
    }

    return user


@timer
def factorial(n: int) -> int:
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

print(create_user("test", ""))