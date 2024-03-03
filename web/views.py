from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse
from .models import Article, Category
from .forms import ContactForm


class BaseArticlesListView(generic.ListView):
    model = Article
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Puedes agregar aquí cualquier otro contexto común que necesites para todas las vistas
        return context


class IndexArticlesListView(BaseArticlesListView):
    template_name = 'web/index.html'
    context_object_name = 'articles' 
    
    def get_queryset(self):
        return Article.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Aquí puedes agregar cualquier otro contexto que necesites
        return context



class LastNewsListView(BaseArticlesListView):
    template_name = 'web/last-news.html'
    
    def get_queryset(self):
        return Article.objects.order_by("-publication_date")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Últimas noticias'  # Añadir un título de página
        return context


class ArticlesByCategoryListView(BaseArticlesListView):
    template_name = 'web/category.html'
    
    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        category = Category.objects.get(slug=category_slug)
        return Article.objects.filter(categories=category)


class ArticleDetailView(generic.DetailView):
    model = Article
    template_name = "web/detail.html"


def detail(request, article_slug):
    article = Article.objects.get(slug=article_slug)
    context = {
        'article': article
    }
    return render(request, 'web/detail.html', context)


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
