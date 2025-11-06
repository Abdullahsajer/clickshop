from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# ✅ تخصيص واجهة لوحة التحكم
admin.site.site_header = "لوحة التحكم - متجر كليك شوب"
admin.site.site_title = "لوحة التحكم"
admin.site.index_title = "مرحبًا بك في لوحة الإدارة"

urlpatterns = [
    path('admin/', admin.site.urls),

    # ✅ روابط التطبيقات الداخلية
    path('', include('store.urls')),         # الصفحة الرئيسية تعرض المنتجات
    path('accounts/', include('accounts.urls')),  # مسارات الحساب وتسجيل الدخول
    path('orders/', include('orders.urls')),       # مسارات السلة والطلبات
]

# ✅ ربط ملفات media و static في وضع التطوير فقط
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
