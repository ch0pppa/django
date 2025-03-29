from django.urls import path
from goods import views

app_name = 'main'

urlpatterns = [
    path('', views.catalog, name='index'),
    path('about/', views.about_view, name='about'),
    path('product/', views.product, name='product'),   
]