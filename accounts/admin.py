from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'phone', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('المعلومات الشخصية', {'fields': ('first_name', 'last_name', 'email', 'phone', 'address')}),
        ('الصلاحيات', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('تواريخ مهمة', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone', 'address')}),
    )
