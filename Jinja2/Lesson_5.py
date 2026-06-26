# Lesson 5
# Фильтры и макросы

from jinja2 import *

cars = [
    {'model': 'Audi', 'price': 2300},
    { 'model': 'BMW', 'price': 2000 },
    {'model': 'Mers', 'price': 2000 },
    {'model': 'Posch', 'price': 2000 },
    ]

tpl = ("Суммарная цена автомобилей {{ (cs | max(attribute='price')).model }}")
tm = Template(tpl)
mgs = tm.render(cs=cars)

print(mgs)