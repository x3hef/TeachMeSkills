# Lesson 2

from jinja2 import Template


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


per = Person("Pasha", 18)

tm = Template("Мне {{ p.age }}, и зовут {{ p.name }}")
msg = tm.render(p=per)
print(msg)