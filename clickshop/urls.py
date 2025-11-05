from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # App URLs
    path('', include('store.urls')),         # الصفحة الرئيسية تعرض المنتجات
    path('accounts/', include('accounts.urls')),  # مسارات الحساب وتسجيل الدخول
    path('orders/', include('orders.urls')),       # مسارات السلة والطلبات
]
