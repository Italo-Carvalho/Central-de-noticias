from django.urls import path
from .views import IndexView, PostDetailView, CategoriaView, TagsView, SearchResultsView

urlpatterns = [
    path('', IndexView.as_view(), name='Index'),
    path('noticias/<slug:slug>', PostDetailView.as_view(), name='detail'),
    path('categoria/<slug:slug>', CategoriaView.as_view(), name='categoria'),
    path('tag/<slug:slug>', TagsView.as_view(), name='tag'),
    path('search/', SearchResultsView.as_view(), name='search_results'),

]
