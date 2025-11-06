from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'available', 'created_at')
    list_filter = ('available', 'created_at', 'category')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
