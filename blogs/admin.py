from django.contrib import admin
from .models import Blogs


@admin.register(Blogs)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "contents", "preview", "created_at", "is_activ", "count_views")
    list_filter = ("title", "created_at")
    search_fields = (
        "title",
        "contents",
        "created_at",
        "is_activ"
    )
