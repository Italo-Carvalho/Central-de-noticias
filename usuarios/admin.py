from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUsuarioChangeForm, CustomUsuarioCreateForm
from .models import CustomUsuario


@admin.register(CustomUsuario)
class CustomUsuarioAdmin(UserAdmin):
    add_form = CustomUsuarioCreateForm
    form = CustomUsuarioChangeForm
    model = CustomUsuario
    list_display = ('username', 'first_name', 'criado', 'get_groups')

    def get_groups(self, obj):
        return obj.groups.values_list('name', flat=True).get(pk=1)

    get_groups.short_description = 'Groupos'

    fieldsets = (
        (None, {
            'fields': ('username', 'password', 'first_name', "last_name", "bio", 'avatar',
                       'is_active', 'is_staff', 'is_superuser', 'groups',

                       )}),

    )
