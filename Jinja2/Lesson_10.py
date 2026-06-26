from jinja2 import Environment, FileSystemLoader, FunctionLoader

persons = [
    {"name": "", "age": 25},
    {"name": "", "age": 25},
    {"name": "", "age": 25},
    {"name": "", "age": 25},
]

def load_tpl(path):
    if path == "index":
        return '''{{u.name}}'''
    else:
        return '''{{u}}'''


# file_loader = FileSystemLoader('templates')
file_loader = FunctionLoader(load_tpl)
env = Environment(loader=file_loader)


tm = env.get_template('index') # Template
mgs = tm.render(u=persons[0]) # обработка шаблона
print(mgs)