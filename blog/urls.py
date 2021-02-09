from django.urls import path
from .views import IndexView, PostDetailView, TagsView, SearchResultsView, CategoriaDetail

urlpatterns = [
    path('', IndexView, name='Index'),
    path('noticias/<slug:slug>', PostDetailView.as_view(), name='detail'),
    path('categoria/<slug:slug>', CategoriaDetail, name='categoria'),
    path('tag/<slug:slug>', TagsView, name='tag'),
    path('search', SearchResultsView, name='search_results'),

]
