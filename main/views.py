from django.http import HttpResponse
from django.shortcuts import render
from django.template import context

def index(request):
    context = {
        'title': 'Домашняя страница',
        'content': 'Магазин мебели HOME'
    }
    
    return render(request, 'main/index.html', context)

def  about(request):
    context = {
        'title': 'Домашняя страница - О нас',
        'content': 'О нас',
        'text_on_page': 'Добро пожаловать в наш мебельный магазин!'

    }
    
    return render(request, 'main/about.html', context)
    
    