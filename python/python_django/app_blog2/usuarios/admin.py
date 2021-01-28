from django import contrib
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class AdminRegisterUser(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'rut', 'user_n', 'password', 'last_login')}),
        ('permissions', {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions',
        )}),
    )

    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'rut', 'password1', 'password2')
            }
        )
    )

    list_display = ('email', 'name', 'is_staff', 'last_login')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions')

admin.site.register(CustomUser)

# Register your models here.
