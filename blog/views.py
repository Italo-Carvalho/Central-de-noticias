from django.shortcuts import render
from .models import Post, Tags
from django.views.generic import ListView, DetailView


class IndexView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    paginate_by = 1
    queryset = Post.objects.all()


class PostDetailView(DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'post'
