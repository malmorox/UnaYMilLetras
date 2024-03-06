from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from django.utils.text import slugify


class Author(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)  # Relación uno a uno con el modelo User
    photo = models.ImageField(upload_to='author_photos/', null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username


class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug: # Si el slug no está definido
            self.slug = slugify(self.name) # Genera el slug a partir del nombre en una versión legible para URL 
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=80)
    content = HTMLField()
    publication_date = models.DateTimeField(auto_now_add=True)
    preview_image = models.ImageField(upload_to='article_images/', null=True, blank=True)
    categories = models.ManyToManyField(Category)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug: # Si el slug no está definido
            self.slug = slugify(self.title) # Genera el slug a partir del titulo en una versión legible para URL
        super().save(*args, **kwargs)
    
    def __str__(self):  
        return self.title 


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField(max_length=255)
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return f'Comentario de {self.author} en "{self.article.title}"'
