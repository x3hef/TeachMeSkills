# Задание 3

def isAnagram(s, t):
    if sorted(s) == sorted(t):
        return True
    return False


