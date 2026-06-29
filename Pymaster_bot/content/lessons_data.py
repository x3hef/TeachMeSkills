LESSON_ORDER = ['variables',
                'types',
                'strings',
                'numbers',
                'input_output',
                'conditions',
                'logic',
                'for_loop',
                'while_loop',
                'lists',
                'dicts',
                'tuples_sets',
                'functions',
                'exceptions',
                'files',
                'modules',
                'oop_basics',
                'classes_objects',
                'inheritance']


LESSONS = {'variables': {'title': 'Переменные',
               'text': 'Переменная — это основа любой программы в Python.\n'
                       '\n'
                       'Она позволяет хранить данные в памяти и использовать их позже.\n'
                       '\n'
                       'Представь коробку с ярлыком — внутри может быть число, текст или любой '
                       'другой объект.\n'
                       '\n'
                       'Без переменных невозможно писать программы, потому что данные просто негде '
                       'хранить.',
               'code': "name = 'Emre'\nage = 20",
               'idea': 'Переменные позволяют сохранять и переиспользовать данные в коде.',
               'practice': {'task': 'Создай переменные name и age с твоими данными'},
               'video': 'https://www.youtube.com/results?search_query=python+переменные+урок',
               'docs': 'https://docs.python.org/3/tutorial/introduction.html',
               'article': 'https://www.w3schools.com/python/python_variables.asp'},
 'types': {'title': 'Типы данных',
           'text': 'В Python каждое значение имеет свой тип.\n'
                   '\n'
                   'Тип данных определяет, как программа будет работать с этим значением.\n'
                   '\n'
                   'Например:\n'
                   '• числа используются для математики\n'
                   '• строки для текста\n'
                   '• логические значения для условий\n'
                   '\n'
                   'Python автоматически определяет тип, но важно понимать их различия.',
           'code': "x = 10\nname = 'Emre'\nis_student = True",
           'idea': 'Тип данных определяет поведение значения в программе.',
           'practice': {'task': 'Создай 3 переменные разных типов данных'},
           'video': 'https://www.youtube.com/results?search_query=python+типы+данных',
           'docs': 'https://docs.python.org/3/library/stdtypes.html',
           'article': 'https://www.w3schools.com/python/python_datatypes.asp'},
 'strings': {'title': 'Строки',
             'text': 'Строка — это текст в Python.\n'
                     '\n'
                     'Она всегда заключается в кавычки: \' \' или " ".\n'
                     '\n'
                     'Строки можно складывать, изменять и анализировать.\n'
                     '\n'
                     'Это один из самых часто используемых типов данных в программировании.',
             'code': 'text = \'Hello Python\'\nname = "Emre"',
             'idea': 'Строки используются для работы с текстовой информацией.',
             'practice': {'task': 'Создай строку с твоим именем и городом'},
             'video': 'https://www.youtube.com/results?search_query=python+строки',
             'docs': 'https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str',
             'article': 'https://www.w3schools.com/python/python_strings.asp'},
 'numbers': {'title': 'Числа',
             'text': 'Числа в Python используются для математических операций.\n'
                     '\n'
                     'Есть два основных типа:\n'
                     '• int — целые числа\n'
                     '• float — числа с точкой\n'
                     '\n'
                     'С их помощью можно выполнять любые вычисления.',
             'code': 'a = 10\nb = 2.5\nresult = a + b',
             'idea': 'Числа используются для вычислений и логики программ.',
             'practice': {'task': 'Сложи два числа и выведи результат'},
             'video': 'https://www.youtube.com/results?search_query=python+числа',
             'docs': 'https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex',
             'article': 'https://www.w3schools.com/python/python_numbers.asp'},
 'input_output': {'title': 'Ввод и вывод',
                  'text': 'В Python можно взаимодействовать с пользователем.\n'
                          '\n'
                          'Функция input() позволяет получать данные.\n'
                          'Функция print() выводит информацию на экран.\n'
                          '\n'
                          'Это основа интерактивных программ.',
                  'code': "name = input('Введите имя: ')\nprint('Привет', name)",
                  'idea': 'Ввод и вывод позволяют общаться с пользователем.',
                  'practice': {'task': 'Сделай программу, которая спрашивает имя'},
                  'video': 'https://www.youtube.com/results?search_query=python+input+print',
                  'docs': 'https://docs.python.org/3/library/functions.html#input',
                  'article': 'https://www.w3schools.com/python/python_user_input.asp'},
 'conditions': {'title': 'Условия',
                'text': 'Условия позволяют программе принимать решения.\n'
                        '\n'
                        'С помощью if можно выполнять код только при выполнении условия.\n'
                        '\n'
                        'Это основа логики любой программы.',
                'code': "if 5 > 3:\n    print('Да')",
                'idea': 'Условия позволяют программе принимать решения.',
                'practice': {'task': 'Проверь, больше ли твой возраст 18'},
                'video': 'https://www.youtube.com/results?search_query=python+if+else',
                'docs': 'https://docs.python.org/3/tutorial/controlflow.html',
                'article': 'https://www.w3schools.com/python/python_conditions.asp'},
 'logic': {'title': 'Логические операторы',
           'text': 'Логические операторы используются для работы с условиями.\n'
                   '\n'
                   'Основные:\n'
                   '• and — и\n'
                   '• or — или\n'
                   '• not — не\n'
                   '\n'
                   'Они помогают строить сложные условия.',
           'code': 'True and False\nTrue or False\nnot True',
           'idea': 'Логика используется в условиях и проверках.',
           'practice': {'task': 'Создай условие с and или or'},
           'video': 'https://www.youtube.com/results?search_query=python+логические+операторы',
           'docs': 'https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not',
           'article': 'https://www.w3schools.com/python/python_operators.asp'},
 'for_loop': {'title': 'Цикл for',
              'text': 'Цикл for используется для повторения действий.\n'
                      '\n'
                      'Он позволяет пройтись по последовательности значений.\n'
                      '\n'
                      'Очень часто используется в программировании.',
              'code': 'for i in range(5):\n    print(i)',
              'idea': 'Цикл for используется для повторения действий.',
              'practice': {'task': 'Выведи числа от 0 до 10'},
              'video': 'https://www.youtube.com/results?search_query=python+for+loop',
              'docs': 'https://docs.python.org/3/tutorial/controlflow.html#for-statements',
              'article': 'https://www.w3schools.com/python/python_for_loops.asp'},
 'while_loop': {'title': 'Цикл while',
                'text': 'Цикл while выполняет код, пока условие истинно.\n'
                        '\n'
                        'Он используется, когда количество повторений неизвестно заранее.',
                'code': 'i = 0\nwhile i < 5:\n    i += 1',
                'idea': 'Цикл while работает пока условие истинно.',
                'practice': {'task': 'Сделай цикл while'},
                'video': 'https://www.youtube.com/results?search_query=python+while',
                'docs': 'https://docs.python.org/3/reference/compound_stmts.html#while',
                'article': 'https://www.w3schools.com/python/python_while_loops.asp'},
 'functions': {'title': 'Функции',
               'text': 'Функции позволяют объединять код в блоки.\n'
                       '\n'
                       'Это помогает избегать повторений и делает код чище.\n'
                       '\n'
                       'Функции можно вызывать много раз.',
               'code': "def hello():\n    print('Hi')",
               'idea': 'Функции позволяют переиспользовать код.',
               'practice': {'task': 'Создай простую функцию'},
               'video': 'https://www.youtube.com/results?search_query=python+functions',
               'docs': 'https://docs.python.org/3/tutorial/controlflow.html#defining-functions',
               'article': 'https://www.w3schools.com/python/python_functions.asp'},
 'lists': {'title': 'Списки',
           'text': 'Список — это структура данных, которая хранит много значений.\n'
                   '\n'
                   'Списки могут изменяться и содержать любые типы данных.',
           'code': 'nums = [1, 2, 3]',
           'idea': 'Списки хранят набор данных.',
           'practice': {'task': 'Создай список из 5 чисел'},
           'video': 'https://www.youtube.com/results?search_query=python+списки',
           'docs': 'https://docs.python.org/3/tutorial/datastructures.html#more-on-lists',
           'article': 'https://www.w3schools.com/python/python_lists.asp'},
 'dicts': {'title': 'Словари',
           'text': 'Словарь хранит данные в формате ключ: значение.\n'
                   '\n'
                   'Это очень удобная структура для работы с объектами.',
           'code': "user = {'name': 'Emre', 'age': 20}",
           'idea': 'Словари хранят данные по ключам.',
           'practice': {'task': 'Создай словарь пользователя'},
           'video': 'https://www.youtube.com/results?search_query=python+словари',
           'docs': 'https://docs.python.org/3/tutorial/datastructures.html#dictionaries',
           'article': 'https://www.w3schools.com/python/python_dictionaries.asp'},
 'tuples_sets': {'title': 'Кортежи и множества',
                 'text': 'Кортеж — неизменяемый список.\n'
                         'Множество — набор уникальных значений.\n'
                         '\n'
                         'Они используются для разных задач обработки данных.',
                 'code': 't = (1, 2, 3)\ns = {1, 2, 3}',
                 'idea': 'Разные типы коллекций данных.',
                 'practice': {'task': 'Создай tuple и set'},
                 'video': 'https://www.youtube.com/results?search_query=python+кортежи+множества',
                 'docs': 'https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences',
                 'article': 'https://www.w3schools.com/python/python_tuples.asp'},
 'exceptions': {'title': 'Исключения',
                'text': 'Исключения позволяют обрабатывать ошибки.\n'
                        '\n'
                        'С их помощью программа не падает при сбоях.',
                'code': "try:\n    1/0\nexcept:\n    print('error')",
                'idea': 'Обработка ошибок делает программу стабильной.',
                'practice': {'task': 'Сделай try/except'},
                'video': 'https://www.youtube.com/results?search_query=python+исключения+try+except',
                'docs': 'https://docs.python.org/3/tutorial/errors.html',
                'article': 'https://www.w3schools.com/python/python_try_except.asp'},
 'files': {'title': 'Файлы',
           'text': 'Python умеет работать с файлами.\n'
                   '\n'
                   'Можно читать, записывать и изменять данные.',
           'code': "open('file.txt', 'r')",
           'idea': 'Работа с файлами — основа backend.',
           'practice': {'task': 'Открой файл и прочитай данные'},
           'video': 'https://www.youtube.com/results?search_query=python+работа+с+файлами',
           'docs': 'https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files',
           'article': 'https://www.w3schools.com/python/python_file_handling.asp'},
 'modules': {'title': 'Модули',
             'text': 'Модули позволяют подключать готовый код.\n'
                     '\n'
                     'Это ускоряет разработку и расширяет возможности Python.',
             'code': 'import math',
             'idea': 'Модули расширяют возможности Python.',
             'practice': {'task': 'Импортируй модуль math'},
             'video': 'https://www.youtube.com/results?search_query=python+модули+import',
             'docs': 'https://docs.python.org/3/tutorial/modules.html',
             'article': 'https://www.w3schools.com/python/python_modules.asp'},
 'oop_basics': {'title': 'ООП основы',
                'text': 'ООП — это подход, где программа состоит из объектов.\n'
                        '\n'
                        'Объекты имеют свойства и поведение.',
                'code': 'class A:\n    pass',
                'idea': 'ООП помогает структурировать код.',
                'practice': {'task': 'Создай класс'},
                'video': 'https://www.youtube.com/results?search_query=python+ооп+для+начинающих',
                'docs': 'https://docs.python.org/3/tutorial/classes.html',
                'article': 'https://www.w3schools.com/python/python_classes.asp'},
 'classes_objects': {'title': 'Классы и объекты',
                     'text': 'Классы — это шаблоны.\nОбъекты — это экземпляры классов.',
                     'code': 'obj = A()',
                     'idea': 'Классы создают объекты.',
                     'practice': {'task': 'Создай объект класса'},
                     'video': 'https://www.youtube.com/results?search_query=python+классы+и+объекты',
                     'docs': 'https://docs.python.org/3/tutorial/classes.html#a-first-look-at-classes',
                     'article': 'https://www.w3schools.com/python/python_classes.asp'},
 'inheritance': {'title': 'Наследование',
                 'text': 'Наследование позволяет создавать новые классы на основе старых.\n'
                         '\n'
                         'Это помогает переиспользовать код.',
                 'code': 'class B(A):\n    pass',
                 'idea': 'Наследование расширяет функциональность классов.',
                 'practice': {'task': 'Сделай наследование классов'},
                 'video': 'https://www.youtube.com/results?search_query=python+наследование+классов',
                 'docs': 'https://docs.python.org/3/tutorial/classes.html#inheritance',
                 'article': 'https://www.w3schools.com/python/python_inheritance.asp'}}
