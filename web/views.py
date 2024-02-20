from django.shortcuts import render
from django.http import HttpResponse
from .models import Article


def index(request):
    all_articles = Article.objects.order_by("-publication_date")
    context = {
        'all_articles': all_articles
    }
    return render(request, "web/index.html", context)


def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    context = {
        'article': article
    }
    return render(request, 'web/detail.html', context)


#def article_list(request):
    #articles = Article.objects.all()
    #return render(request, 'article_list.html', {'articles': articles})


def contact(request):
    article = Article.objects.get(id=article_id)
    context = {
        'article': article
    }
    return render(request, 'web/contact.html', context)
