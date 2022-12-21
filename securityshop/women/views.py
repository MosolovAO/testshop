from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import *


menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'},
]



def index(request):
    posts = Women.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница',
    }
    return render(request, 'women/index.html', context=context)


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})


def categories(request, catid):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1> <p> {catid} </p>")


def show_post(request, post_id):
    return HttpResponse(f"<h2>Страница поста №{post_id}</h2>")


def add_page(request):
    return HttpResponse(f"<h2>Страница добавления статей</h2>")


def contact(request):
    return HttpResponse(f"<h2>Страница обратной связи</h2>")


def login(request):
    return HttpResponse(f"<h2>Страница входа</h2>")


def pagenotfound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")