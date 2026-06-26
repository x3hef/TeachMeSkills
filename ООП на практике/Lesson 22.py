# Наследование

class Doctor: # - Родительский класс

    def can_walk(self):
        print("can_walk")

    def can__cure(self):
        print("can_cure")


class Student(Doctor): # - под класс

    def can_stu(self):
        print("can_stu")

print(issubclass(Student, Doctor))
print(issubclass(Doctor, Student))
