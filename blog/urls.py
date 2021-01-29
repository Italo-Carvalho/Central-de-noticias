from django.urls import path
from .views import IndexView, DetailView

urlpatterns = [
    path('', IndexView.as_view(), name='Index'),
    path('<slug:slug>/', DetailView.as_view(), name='detail')
]
