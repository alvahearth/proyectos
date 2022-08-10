from typing import no_type_check_decorator
from django.contrib import admin
from django.contrib.admin.helpers import AdminForm
from django.db import models
from django.db.models.base import ModelStateFieldsCacheDescriptor
from .models import Articulo, Category, Comments

class ArticuloAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")

    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id

        obj.save()

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", )

admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comments)

# Register your models here.
