from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import *


def index(request):
    posts = Women.objects.all()
    context = {
        'posts': posts,
        'title': 'Главная страница',
        'category_selected': 0,
    }
    return render(request, 'women/index.html', context=context)


def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте'})


def show_post(request, post_id):
    return HttpResponse(f"<h2>Страница поста №{post_id}</h2>")


def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)
    context = {
        'posts': posts,
        'title': 'Главная страница',
        'category_selected': cat_id,
    }
    return render(request, 'women/index.html', context=context)


def add_page(request):
    return HttpResponse(f"<h2>Страница добавления статей</h2>")


def contact(request):
    return HttpResponse(f"<h2>Страница обратной связи</h2>")


def login(request):
    return HttpResponse(f"<h2>Страница входа</h2>")


def pagenotfound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")