from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin

from .models import *


class PostResource(resources.ModelResource):
    class Meta:
        model = Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["name", "birth_year", "death_year"]
    search_fields = ["name"]


@admin.register(Book)
class BookAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ["id", "title", "available", "publication_year"]
    search_fields = ["title"]
    # list_filter = ["available", "publication_year", "authors"]
    resource_class = PostResource


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "category_description"]
    search_fields = ["name"]
