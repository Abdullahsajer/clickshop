from django.contrib import admin
from django.urls import path, include
from django.contrib import admin

admin.site.site_header = "لوحة التحكم - متجر كليك شوب"
admin.site.site_title = "لوحة التحكم"
admin.site.index_title = "مرحبًا بك في لوحة الإدارة"



urlpatterns = [
    path('admin/', admin.site.urls),

    # App URLs
    path('', include('store.urls')),         # الصفحة الرئيسية تعرض المنتجات
    path('accounts/', include('accounts.urls')),  # مسارات الحساب وتسجيل الدخول
    path('orders/', include('orders.urls')),       # مسارات السلة والطلبات
]
