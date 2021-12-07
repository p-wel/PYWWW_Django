from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "created", "modified", "published"]
    search_fields = ["title", "description"]
    list_filter = ["published"]
