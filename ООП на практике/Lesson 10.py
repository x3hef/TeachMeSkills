# практика с property
import string


class User:
    def __init__(self, login, password):
        self.login = login
        self.__password = password

    @property
    def password(self):
        return self.__password

    @staticmethod
    def check(password):
        for digit in password:
            if digit not in password:
                return True
        return False

    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise TypeError("Password must be a string")
        if len(value) < 4:
            raise ValueError("Password must be at least 4 characters")
        if len(value) > 16:
            raise ValueError("Password must be at most 16 characters")
        if not User.check(value):
            raise ValueError("Password must contain only letters, numbers and underscores")
        self.__password = value
