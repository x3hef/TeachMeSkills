from jinja2 import Template

persons = [
    {"name": "Pasha", "age": 22},
    {"name": "Alex", "age": 15},
    {"name": "Lexa", "age": 21},
    {"name": "Dima", "age": 23},
    {"name": "Oleg", "age": 25},
]

html = '''
{% macro list_users(list_of_user) -%}
<ul>
{% for u in list_of_user -%}
    <li>
        {{ u.name }}
        {{ caller(u) }}
    </li>
{% endfor %}
</ul>
{% endmacro %}

{% call(user) list_users(users) %}
    <ul>
        <li>age: {{ user.age }}</li>
    </ul>
{% endcall %}
'''

tm = Template(html)
mgs = tm.render(users=persons)
print(mgs)