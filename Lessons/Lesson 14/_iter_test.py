from typing import Iterator
from typing import List

text = "Hello World"

list1 = [1, 2, 3]

iter_list: Iterator = iter(list1)
iter_text: Iterator = iter(text)

print(next(iter_list))

print(type(iter_list))


