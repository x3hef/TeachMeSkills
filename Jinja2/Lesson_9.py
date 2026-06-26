from jinja2 import Environment, FileSystemLoader

link = '''<select name="cities"> 
{% for city in cities %}
    <option value="{{c["id"]}}">{{c["citi"]}}</option>
    {% endfor %}
    </select>

'''