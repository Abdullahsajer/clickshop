from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("معلومات إضافية", {"fields": ("phone", "address")}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
