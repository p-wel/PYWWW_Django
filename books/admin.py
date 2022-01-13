from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib import admin
from django.forms import forms
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Book, Author, Category


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["name", "birth_year", "death_year"]
    search_fields = ["name"]


class BookResource(resources.ModelResource):
    class Meta:
        model = Book


@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    list_display = ["id", "title"]
    search_fields = ["title", "description", "author"]
    list_filter = ["available"]
    resource_class = BookResource


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["name"]


class BookBorrowForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('borrow', 'Wypożycz'))
