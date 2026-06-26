a_input = input("Число a: ")
b_input = input("Число b: ")
c_input = input("Число c: ")


# a_input.isdigit() and b_input.isdigit() and c_input.isdigit().
# True and True and True.
# True.


# a_input.isdigit() and b_input.isdigit() and c_input.isdigit().
# True and False and True.
# False.

if a_input.isdigit() and b_input.isdigit() and c_input.isdigit():
    a = int(a_input)
    b = int(b_input)
    c = int(c_input)

    print(a * b * c)


# a_input.isdigit() or b_input.isdigit() or c_input.isdigit().
# True or False or True.
# True.

if a_input.isdigit() or b_input.isdigit() or c_input.isdigit():
    print("Хотя бы одно значение является числовым.")


if a_input.isdigit() and b_input.isdigit() or c_input.isdigit():
    print("Хотя бы одно значение является числовым.")