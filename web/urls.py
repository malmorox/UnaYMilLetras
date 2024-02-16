from . import views
from django.urls import path

app_name = 'UnaYMilLetras'

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
    path('contact/', views.contact, name='contact'),
]