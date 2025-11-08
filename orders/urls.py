from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('cart/', views.order_view, name='order_view'),  # ✅ عرض السلة
    path('add-to-order/<int:product_id>/', views.add_to_order, name='add_to_order'),  # ✅ إضافة منتج للسلة
    path('checkout/', views.checkout_view, name='checkout'),  # ✅ إتمام الطلب
    path('order-success/<int:order_id>/', views.order_success_view, name='order_success'),  # ✅ نجاح الطلب
    path('my-orders/', views.orders_list_view, name='orders_list'),  # ✅ قائمة الطلبات السابقة
]
