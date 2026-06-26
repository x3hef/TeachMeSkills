from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.


menu = ['о сайте', 'Добавить статью', 'Обратная связь', 'Войти']




def index(request): # ссылка на спец класс HttpRequest.
    # t = render_to_string("index.html")
    # return HttpResponse(t)
    data = {'title': 'Главная страница!',
            "menu": menu,
            "float": 26.34,
            "lst": [1,23,23,43],
            "set": {1,2,3,4,5},
            "dict": {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5},
            }
    return render(request,"women/index.html", data)

def about(request):
    data = {'title': 'О сайте!',
            "menu": menu}
    return render(request, "women/about.html", data)

def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи c id = {post_id}")

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Старница не найдены</h1>") # - HTTP/1.1" 404
