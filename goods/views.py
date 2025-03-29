from django.shortcuts import render

def about_view(request):
    context = {
        'content': 'О нас',
        'text_on_page': 'Добро пожаловать на наш сайт',
        'elevenlabs_agent_id': '2Z4GUrI2wwqbwSehUdwQ'  # Передаем ID в шаблон
    }
    return render(request, 'main/about.html', context)

def catalog(request):
    return render(request, 'goods/catalog.html')

def product(request):
    return render(request, 'goods/product.html')
