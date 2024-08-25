from django.contrib import admin
from .models import CustomUser, TimeBasedStampModel


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "phone_number",
        "date_of_birth",
        "is_active",
        "is_staff",
    )
    search_fields = ("username", "phone_number")
    list_filter = ("is_active", "is_staff")
