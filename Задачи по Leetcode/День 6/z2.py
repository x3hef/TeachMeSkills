# Задание 2


def palindrome(n: str):
    n = n.lower().replace(" ", "")

    if n == n[::-1]:
        return True
    else:
        return False

print(palindrome(input()))