from django.shortcuts import render
from .models import Post, Tags, Categorias
from django.views.generic import ListView, DetailView, TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'
    #model = Post
    #context_object_name = 'posts'
    #paginate_by = 8
    #queryset = Post.objects.all().order_by('-criados')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-criados')[:8]
        context['categorias'] = Categorias.objects.all().order_by(
            '-criados')[:10]
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
