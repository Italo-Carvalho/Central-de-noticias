from django.shortcuts import render
from .models import Post, Tags, Categorias
from django.views.generic import ListView, DetailView, TemplateView
from django.db.models import Q


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-criados')[:8]
        context['categorias'] = Categorias.objects.all().order_by(
            '-criados')[:10]
        return context


class CategoriaView(DetailView):
    model = Categorias
    template_name = 'categoria.html'
    context_object_name = 'categoria'

    def get_context_data(self, **kwargs):
        context = super(CategoriaView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-criados')[:6]
        context['categorias'] = Categorias.objects.all().order_by(
            '-criados')[:10]
        return context


class TagsView(DetailView):
    model = Tags
    template_name = 'tag.html'
    context_object_name = 'categoria'

    def get_context_data(self, **kwargs):
        context = super(TagsView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-criados')[:6]
        context['categorias'] = Tags.objects.all().order_by(
            '-criados')[:10]
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-criados')[:4]
        context['categorias'] = Categorias.objects.all().order_by(
            '-criados')[:10]
        return context


class SearchResultsView(ListView):
    model = Post
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(
            Q(titulo__icontains=query) | Q(sub_titulo__icontains=query)
        )

        return object_list
