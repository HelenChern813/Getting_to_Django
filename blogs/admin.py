from django.contrib import admin
from .models import Blogs


@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "contents", "preview", "created_at", "is_active", "views_count")
    list_filter = ("title", "created_at")
    search_fields = ("title", "contents", "created_at", "is_active")
