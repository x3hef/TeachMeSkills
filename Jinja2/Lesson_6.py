# Lesson 6

from jinja2 import *

cars = [
    {'model': 'Audi', 'price': 2300},
    {'model': 'BMW', 'price': 2000 },
    {'model': 'Mers', 'price': 2000 },
    {'model': 'Posch', 'price': 2000 },
    ]

tpl = '''
{%- for u in cars -%}
{% filter upper %}{{u.model}}{% endfilter %}
{% filter lower %}{{u.model}}{% endfilter %}
{% endfor %}
'''

tm = Template(tpl)
mgs = tm.render(cars = cars)
print(mgs)