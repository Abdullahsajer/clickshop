from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'paid', 'created_at')
    list_filter = ('paid', 'created_at')
    search_fields = ('user__username',)
    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price')
