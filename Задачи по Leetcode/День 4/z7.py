# Задание 7

class Employee:
    def __init__(self, name: str, salary: int) -> None:
        self._name = name
        self.salary = salary

    def get_salary(self):
        return self.salary

class Manager(Employee):
    def __init__(self,bonus: int, name: str, salary: int):
        super().__init__(name, salary)
        self.bonus = bonus

    def get_bonus(self):
        return self.bonus + self.bonus


class Developer(Employee):
    def __init__(self,hours_worked: int, hour_rate: int, name: str, salary: int):
        super().__init__(name, salary)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def get_salary(self):
        return self.hours_worked * self.hour_rate
