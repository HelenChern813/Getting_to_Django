from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
        "phone_number",
        "country",
        "avatar",
        "username",
        "first_name",
        "last_name",
        "is_active",
    )
    list_filter = ("email", "country", "username", "is_active")
    search_fields = ("country", "country", "phone_number")
