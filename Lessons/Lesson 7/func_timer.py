import time
import random
import string


def user_password_generator(max_length: int = 12) -> str:
    passwd = ""
    for i in range(max_length):
        passwd += random.choice(string.ascii_letters + string.digits)

    return passwd


def create_user(username: str, email: str) -> dict:
    user = {
        'username': username,
        'email': email,
        'password': user_password_generator(),
    }

    return user


def factorial(n: int) -> int:
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def timer(func, *args, **kwargs):
    start_time = time.perf_counter()

    res = func(*args, **kwargs)

    end_time = time.perf_counter()

    print(f'Function: {func.__name__} {args}, {kwargs} | Time taken: {end_time - start_time} seconds')

    return res


for i in [100, 500, 1000]:
    res = timer(factorial, i)