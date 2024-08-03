from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminChangeForm, UserAdminCreationForm
from .models import User


class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ["username", "email", "phone"]
    list_filter = ["is_superuser", "is_active"]

    fieldsets = [
        ("Identifire", {"fields": ["username", "email", "phone"]}),
        (
            "Personal Information",
            {
                "fields": [
                    "password",
                    "first_name",
                    "last_name",
                ]
            },
        ),
        (
            "Permissions",
            {
                "fields": [
                    "is_active",
                    "is_admin",
                    "is_superuser",
                ]
            },
        ),
    ]
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": [
                    "username",
                    "email",
                    "phone",
                    "first_name",
                    "last_name",
                ],
            },
        ),
    ]
    search_fields = ["email", "phone"]
    ordering = ["email"]
    filter_horizontal = []


admin.site.register(User, UserAdmin)
