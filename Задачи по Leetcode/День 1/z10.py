# Задание 10

class Employee:
    count = 0  # атрибут класса для подсчета всех сотрудников

    def __init__(self, name: str, salary: float, email: str):
        self.name = name
        self.salary = salary
        self._email = email
        Employee.count += 1  # увеличиваем счетчик при создании

    # property для email
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Email address must contain @")
        self._email = value

    # обычный метод работы
    def work(self):
        print(f"{self.name} выполняет свои обязанности.")

    # метод для информации о сотруднике
    def info(self):
        print(f"Имя: {self.name}, Зарплата: {self.salary}, Email: {self.email}")

    # класс-метод для подсчета сотрудников
    @classmethod
    def employee_count(cls):
        return cls.count

    # статический метод для проверки бонуса
    @staticmethod
    def is_eligible_bonus(salary):
        return salary >= 5000