import time

cache_dict = {}

def cache(func):

    def wrapper(param):

        if cache_dict.get(param) is None:
            res = func(param)
            cache_dict[param] = res

        return cache_dict[param]

    return wrapper


@cache
def factorial(n: int) -> int:
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


numbers = [100, 200, 300, 500, 200, 800, 900, 1000, 800, 1000, 900, 1000] * 100


result = []

start_time = time.perf_counter()

for n in numbers:
    result.append(factorial(n))

print("Времени потрачено:", time.perf_counter() - start_time)