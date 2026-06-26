# Задание 1

class Student:
    def __init__(self, name: str, grades: list):
        self.name = name
        self.grades = grades

    def add_grade(self, grade: float):
        self.grades.append(grade)

    def get_average(self):
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f'{self.name}, {self.grades}'


class Group:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_students(self):
        for student in self.students:
            print(student)
