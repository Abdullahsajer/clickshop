from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from store import views  # ✅ استيراد دالة home من تطبيق store

# ✅ تخصيص واجهة لوحة التحكم
admin.site.site_header = "لوحة التحكم - متجر كليك شوب"
admin.site.site_title = "لوحة التحكم"
admin.site.index_title = "مرحبًا بك في لوحة الإدارة"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # ✅ الصفحة الرئيسية
    path('accounts/', include('accounts.urls')),
    path('orders/', include('orders.urls')),
]

# ✅ ربط ملفات media و static في وضع التطوير فقط
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
