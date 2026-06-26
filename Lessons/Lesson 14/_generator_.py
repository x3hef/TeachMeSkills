
def number_generator(start: int, stop: int = None, step: int = 1):
    value = start
    while True:
        yield value
        value +=1
        if value > 10:
            break


generator = number_generator()

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
