from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUsuarioChangeForm, CustomUsuarioCreateForm
from .models import CustomUsuario


@admin.register(CustomUsuario)
class CustomUsuarioAdmin(UserAdmin):
    add_form = CustomUsuarioCreateForm
    form = CustomUsuarioChangeForm
    model = CustomUsuario
    list_display = ('username', 'first_name', 'is_staff')

    fieldsets = (
        ('Informações Pessoais', {
            'fields': ('username', 'password', 'first_name', "last_name", "bio", 'avatar')}),
        ('Permissões', {'fields': ('is_active', 'is_staff',
                                   'is_superuser', 'groups')}),
    )
