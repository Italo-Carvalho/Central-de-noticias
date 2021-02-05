from django.urls import path
from .views import UsercreateFormView

urlpatterns = [
    path('', UsercreateFormView.as_view(), name='cadastro'),
]
