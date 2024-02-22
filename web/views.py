from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article, Category
from .forms import ContactForm


def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'web/index.html', context)


def last_news(request):
    last_articles = Article.objects.order_by("-publication_date")
    context = {
        'all_articles': last_articles
    }
    return render(request, "web/last-news.html", context)


def detail(request, article_slug):
    article = Article.objects.get(slug=article_slug)
    context = {
        'article': article
    }
    return render(request, 'web/detail.html', context)


def articles_by_category(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    articles = Article.objects.filter(categories=category)
    context = {
        'category': category,
        'articles': articles
    }
    return render(request, 'web/category.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Procesamos los datos del formulario
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Aquí podrías enviar un correo electrónico, guardar en la base de datos, etc.
            # Por ahora, redireccionamos a una página de éxito
            return redirect('contact_success')
    else:
        form = ContactForm()
        
    context = {
        'form': form
    }
    return render(request, 'web/contact.html', context)
