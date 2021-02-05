from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUsuario
from django import forms


class CustomUsuarioCreateForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, required=True, label='Primeiro nome')
    last_name = forms.CharField(
        max_length=30, required=True, label='Último nome')

    class Meta:
        model = CustomUsuario
        fields = ("username", "first_name", "last_name", "avatar", "bio")

        labels = {
            "bio": "Biografia",
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class CustomUsuarioChangeForm(UserChangeForm):
    class Meta:
        model = CustomUsuario
        fields = ("first_name", "last_name")
