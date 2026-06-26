# Lesson 3
# Способы экранирования

from jinja2 import Template

data = '''{% raw %}Модуль jinja вместо 
определения {{ name }} 
подставляет соответствующие значения{% endraw %}'''

link = '''in HTML: <a href="#">Ссылка</a>''' # е - escape(экранирование)

tm = Template(data)
print(tm.render(name="SSS"))
tm = Template("{{ link | e}}")
print(tm.render(link=link))