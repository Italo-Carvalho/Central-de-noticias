from django.urls import path
from .views import IndexView, PostDetailView, TagsView, SearchResultsView, CategoriaDetail

urlpatterns = [
    path('', IndexView.as_view(), name='Index'),
    path('noticias/<slug:slug>', PostDetailView.as_view(), name='detail'),
    path('categoria/<slug:slug>', CategoriaDetail, name='categoria'),
    path('tag/<slug:slug>', TagsView.as_view(), name='tag'),
    path('search/', SearchResultsView.as_view(), name='search_results'),

]
