from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.views import generic
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
    

class ArticlesByAuthorListView(BaseArticlesListView):
    template_name = 'web/category.html'
    
    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        category = Category.objects.get(slug=category_slug)
        return Article.objects.filter(categories=category)


class ArticleDetailView(generic.DetailView):
    model = Article
    template_name = "web/article-detail.html"
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article_slug = self.kwargs.get('slug')
        article = Article.objects.get(slug=article_slug)
        context['article'] = article
        return context


def contact(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            # Procesamos los datos del formulario
            name = contact_form.cleaned_data['name']
            email = contact_form.cleaned_data['email']
            message = contact_form.cleaned_data['message']
            # Aquí podrías enviar un correo electrónico, guardar en la base de datos, etc.
            # Por ahora, redireccionamos a una página de éxito
            send_mail(
                'Nuevo mensaje de contacto',
                f'Nombre: {name}\nEmail: {email}\nMensaje: {message}',
                'tu@email.com',
                ['destinatario@email.com'],
                fail_silently=False,
            )
            
            return redirect('contact_success')
    else:
        contact_form = ContactForm()
        
    context = {
        'contact_form': contact_form
    }
    return render(request, 'web/contact.html', context)
