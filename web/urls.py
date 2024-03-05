from . import views
from django.urls import path

app_name = 'UnaYMilLetras'

urlpatterns = [
    path('', views.IndexArticlesListView.as_view(), name='article_list'),
    path('ultimas-noticias/', views.LastNewsListView.as_view(), name='last_news'),
    path('articulo/<slug:article_slug>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('categoria/<slug:category_slug>/', views.ArticlesByCategoryListView.as_view(), name='articles_by_category'),
    path('autor/<slug:category_slug>/', views, name='articles_by_category'),
    path('contacto/', views.contact, name='contact')
]
