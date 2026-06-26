# Lesson 4

from jinja2 import *

cities = [{'id': 1, 'city': "Minsk"},
          {'id': 2, 'city': "Berlin"},
          {'id': 3, 'city': "Moskoy"},
          {'id': 4, 'city': "Tver"}]

link = '''<select name="cities">
 {% for c in cities -%}
    <option value="{{ c.city }}">{{ c.city }}</option>
{% endfor -%}
</select>'''

tm = Template(link)
mgs = tm.render(cities=cities)
print(mgs)