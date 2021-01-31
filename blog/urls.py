from django.urls import path
from .views import IndexView, PostDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='Index'),
    path('<slug:slug>/', PostDetailView.as_view(), name='detail')
]
