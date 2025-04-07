
from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Categories

def index(request):
    
    categories = Categories.objects.all()   
    
    context = {
        'title': 'Домашняя страница',
        'content': 'Магазин мебели HOME',
        'categories': categories
    }
    
    return render(request, 'main/index.html', context)

def  about(request):
    context = {
        'title': 'Домашняя страница - О нас',
        'content': 'О нас',
        'text_on_page': 'Добро пожаловать в наш мебельный магазин!'

    }
    
    return render(request, 'main/about.html', context)
    
    