# вариант 39
from jinja2 import Environment, FileSystemLoader,Template
import random

# задание 1
n = 4
b = [random.randint(0, 100) for i in range(n)]

f_template = open('template1.html','r', encoding ='utf-8-sig')
html = f_template.read()
f_template.close()

template = Template(html)

result_html = template.render(name = "b", list = b)
f = open('dz1.html', 'w', encoding ='utf-8-sig')
f.write(result_html)
f.close()

# задание 2
n=4
books = [
    {"title" : "Мастер и Маргарита",
     "author": "Булгаков М.А.",
     "price": 581.50},
    {"title" : "Белая гвардия",
     "author": "Булгаков М.А.",
     "price": 600.00},
    {"title" : "Война и мир",
     "author": "Толстой Л.Н.",
     "price": 899.99},
    {"title" : "Анна Каренина",
     "author": "Толстой Л.Н.",
     "price": 450.10},
    {"title" : "Игрок",
     "author": "Достоевский Ф.М.",
     "price":  234.55}
];

f_template = open('template2.html','r', encoding ='utf-8-sig')
html = f_template.read()
f_template.close()

template = Template(html)

result_html = template.render(list = books, n =n)
f = open('dz2.html', 'w', encoding ='utf-8-sig')
f.write(result_html)
f.close()
