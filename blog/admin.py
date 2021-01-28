from django.contrib import admin
from .models import Post, Categorias, Tags


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('autor', 'titulo', 'ativo', 'modificado')


@admin.register(Categorias)
class CategoriasAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'ativo', 'modificado')


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('tag', 'ativo', 'modificado')
