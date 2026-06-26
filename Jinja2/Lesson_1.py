# Lesson 1

from jinja2 import Template


name = "Федор"

tm = Template("Привет {{name}}")
mgs = tm.render(name=name)
print(mgs)

# {% %} - спецификатор шаблона
# {{ }} - выражение для вставки конструкций Python в шаблон.
# {# #} - блок комментариев
#  # ## - строковый комментарий
