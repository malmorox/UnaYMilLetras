from django.contrib import admin
from .models import Category, Article

from tinymce.widgets import TinyMCE
from django.db import models


# Register your models here.


class ArticleTinyMCE(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TinyMCE()}
    }


admin.site.register(Category)
admin.site.register(Article, ArticleTinyMCE)
