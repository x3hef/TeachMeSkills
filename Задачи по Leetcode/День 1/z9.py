# Задание 9

class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self._email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Email address must be in format: ")
        self._email = value

    @classmethod
    def user_count(cls):
        return cls.count

    @classmethod
    def is_adult(age):
        return age >= 18

    def info(self):
        print(f"{self.name}, {self.age} лет, email: {self.email}")

