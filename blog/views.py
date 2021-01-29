from django.shortcuts import render
from .models import Post, Tags
from django.views.generic import TemplateView, DetailView


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.order_by('criados').all
        return context


class DetailView(DetailView):
    model = Post
    template_name = 'detail.html'
