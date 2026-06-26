# Задание 9

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def is_passed(self):
        if self.grade >= 3:
            return True