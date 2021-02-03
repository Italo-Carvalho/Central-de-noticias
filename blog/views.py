from django.shortcuts import render
from .models import Post, Tags, Categorias
from django.views.generic import ListView, DetailView, TemplateView
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-criados')[:8]
        context['categorias'] = Categorias.objects.all().order_by(
            '-criados')[:10]
        return context


def CategoriaDetail(request, slug):
    categoria = get_object_or_404(Categorias, slug=slug)
    post_list = Post.objects.filter(categoria=categoria)
    page = request.GET.get('page', 2)

    paginator = Paginator(post_list, 2)
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    context = {
        'categoria': categoria,
        'posts': post,
    }
    return render(request, 'categoria.html', context)


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
