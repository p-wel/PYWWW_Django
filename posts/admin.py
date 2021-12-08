from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin

from .models import *


class PostResource(resources.ModelResource):
    class Meta:
        model = Post


@admin.register(Post)
class PostAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ["id", "title", "created", "modified", "published"]
    search_fields = ["title", "description"]
    list_filter = ["published"]
    resource_class = PostResource


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description"]
    search_fields = ["name"]
