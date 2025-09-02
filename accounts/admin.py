from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["username", "email", "name", "is_staff", "is_active"]
    list_filter = ["is_staff", "is_active"]
    fieldsets = (
        (None, {"fields": ("username", "email", "name", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "name", "password1", "password2", "is_staff", "is_active"),
        }),
    )
    # fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("name",)}),)
    # add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("name",)}),)
    

admin.site.register(CustomUser, CustomUserAdmin)