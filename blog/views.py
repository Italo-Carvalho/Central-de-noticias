from django.shortcuts import render
from .models import Post, Tags, Categorias
from django.views.generic import ListView, DetailView, TemplateView
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404


def IndexView(request):
    categorias = Categorias.objects.order_by('?').all
    post_list = Post.objects.all().order_by('-criados')
    post_index = Post.objects.all().order_by('-criados')[:15]
    post_variado = Post.objects.all().order_by('?')[:5]
    page = request.GET.get('page', 1)

    paginator = Paginator(post_list, 7)
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    context = {
        'categorias': categorias,
        'posts': post_index,
        'post': post,
        'post_variado': post_variado,
    }
    return render(request, 'index.html', context)


def CategoriaDetail(request, slug):
    categoria = get_object_or_404(Categorias, slug=slug)
    post_list = Post.objects.filter(categoria=categoria)
    post_index = Post.objects.all().order_by('-criados')[:5]
    page = request.GET.get('page', 1)

    paginator = Paginator(post_list, 8)
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    context = {
        'categoria': categoria,
        'posts': post_index,
        'post_categoria': post,
    }
    return render(request, 'categoria.html', context)


def TagsView(request, slug):
    tags = get_object_or_404(Tags, slug=slug)
    post_list = Post.objects.filter(tags=tags)
    post_index = Post.objects.all().order_by('-criados')[:5]
    page = request.GET.get('page', 1)

    paginator = Paginator(post_list, 8)
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    context = {
        'categoria': tags,
        'posts': post_index,
        'post_tag': post,
    }
    return render(request, 'tag.html', context)


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


def SearchResultsView(request):
    query = request.GET.get('q')
    object_list = Post.objects.filter(
        Q(titulo__icontains=query) | Q(sub_titulo__icontains=query)
    )[:10]
    post_index = Post.objects.all().order_by('-criados')[:5]

    context = {
        'posts': post_index,
        'object_list': object_list,
    }
    return render(request, 'search_results.html', context)
