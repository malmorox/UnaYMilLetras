from . import views
from django.urls import path

app_name = 'UnaYMilLetras'

urlpatterns = [
    path('', views.index, name='article_list'),
    path('ultimas-noticias/', views.last_news, name='last_news'),
    path('articulo/<slug:article_slug>/', views.detail, name='article_detail'),
    path('categoria/<slug:category_slug>/', views.articles_by_category, name='articles_by_category'),
    path('contacto/', views.contact, name='contact')
]
