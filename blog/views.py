from django.shortcuts import render
from .models import Post, Tags
from django.views.generic import ListView, DetailView


class IndexView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    paginate_by = 8
    queryset = Post.objects.all().order_by('-criados')


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
