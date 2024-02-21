from django.db import models
from tinymce.models import HTMLField
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=80)
    content = HTMLField()
    publication_date = models.DateTimeField(auto_now_add=True)
    preview_image = models.ImageField(upload_to='article_images/', null=True, blank=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):  
        return self.title
