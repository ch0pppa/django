from django.shortcuts import get_object_or_404, render
from django.template import context

from goods.models import Products

def about_view(request):
    context = {
        'content': 'О нас',
        'text_on_page': 'Добро пожаловать на наш сайт',
        'elevenlabs_agent_id': '2Z4GUrI2wwqbwSehUdwQ'  # Передаем ID в шаблон
    }
    return render(request, 'main/about.html', context)

def catalog(request, category_slug):
    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = get_object_or_404(Products.objects.filter(category__slug=category_slug)) 
    
    context = {   
        'title': 'Home - Каталог',
        'goods': goods,
    }
    return render(request, 'goods/catalog.html', context)

def product(request, product_slug):
    product= Products.objects.get(slug=product_slug)
    context = {
        'product': product
    }
    return render(request, 'goods/product.html', context=context)
    