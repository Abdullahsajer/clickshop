from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="اسم الفئة")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="المعرف الرابط")
    description = models.TextField(blank=True, null=True, verbose_name="الوصف")

    class Meta:
        verbose_name = "فئة"
        verbose_name_plural = "الفئات"

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE, verbose_name='الفئة'
    )
    name = models.CharField(max_length=255, verbose_name="اسم المنتج")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="المعرف الرابط")
    description = models.TextField(verbose_name="الوصف")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر")
    image = models.ImageField(upload_to='products/%Y/%m/%d', verbose_name="صورة المنتج")
    available = models.BooleanField(default=True, verbose_name="متاح")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإضافة")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="آخر تحديث")

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"
        ordering = ['-created_at']

    def __str__(self):
        return self.name
