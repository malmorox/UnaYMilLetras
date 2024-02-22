from . import views
from django.urls import path

app_name = 'UnaYMilLetras'

urlpatterns = [
    path('', views.index, name='article_list'),
    path('ultimas-noticias/', views.last_news, name='article_list'),
    path('articulo/<int:pk>/', views.detail, name='article_detail'),
    path('categoria/<int:category_id>/', views.articles_by_category, name='articles_by_category'),
    path('contacto/', views.contact, name='contact')
]
