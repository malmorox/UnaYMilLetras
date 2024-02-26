from django.contrib import admin
from django.db import models
from .models import Category, Article
from tinymce.widgets import TinyMCE


# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('slug',)
    formfield_overrides = {
        models.CharField: {'widget': TinyMCE()}
    }
    
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('slug',) 


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
