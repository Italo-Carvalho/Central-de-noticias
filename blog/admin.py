from django.contrib import admin
from .models import Post, Categorias, Tags
from django_summernote.admin import SummernoteModelAdmin
from django.db import models


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('_autor', 'titulo', 'ativo', 'modificado', 'categoria')

    filter_horizontal = ('tags',)
    summernote_fields = ('texto',)

    exclude = ['autor', ]

    def _autor(self, instance):
        return f'{instance.autor.get_full_name()}'

    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(autor=request.user)

    def save_model(self, request, obj, form, change):
        obj.autor = request.user
        super().save_model(request, obj, form, change)


@admin.register(Categorias)
class CategoriasAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'ativo', 'modificado')


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('tag', 'ativo', 'modificado')
