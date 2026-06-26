# магические методы iter next

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def __getitem__(self, key):
        return self.name[key]


    def __iter__(self):
        return self

    def __next__(self):
        return self.name.__next__()


igor = Student('igor', 1)

for key in igor:
    print(key)

