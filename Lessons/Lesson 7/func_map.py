numbers = [1, 3, -23, 0.34, 123, 123.1, 3.14]

# int_numbers = []
# for number in numbers:
#     new_value = func(number)
#     int_numbers.append(new_value)

int_numbers = list(map(int, numbers))

print(int_numbers)

# ==================================================================

numbers2 = [1, 3, -23, 0.3412312, 123, 123.1456456, 3.14938490]

float_numbers = list(map(lambda x: round(float(x), 4), numbers2))

print(float_numbers)

# ==================================================================

numbers3 = [1, 3, -23, 0.3412312, 123, 123.1456456, 3.14938490]

pos_float_numbers = list(
    filter(
        lambda number: number >= 0,
        map(lambda x: round(float(x), 4), numbers2)
    )
)

print(pos_float_numbers)

# ==================================================================

text = "Python это язык программирования"

lower_words = list(map(lambda x: x.lower(), text.split()))

print(lower_words)