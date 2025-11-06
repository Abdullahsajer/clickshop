from django.db import models
from django.conf import settings
from store.models import Product

class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="المستخدم"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الطلب")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="آخر تحديث")
    paid = models.BooleanField(default=False, verbose_name="مدفوع")

    class Meta:
        verbose_name = "طلب"
        verbose_name_plural = "طلبات"
        ordering = ['-created_at']

    def __str__(self):
        return f"طلب رقم {self.id} للمستخدم {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name='items', on_delete=models.CASCADE, verbose_name="الطلب"
    )
    product = models.ForeignKey(
        Product, related_name='order_items', on_delete=models.CASCADE, verbose_name="المنتج"
    )
    quantity = models.PositiveIntegerField(default=1, verbose_name="الكمية")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر")

    class Meta:
        verbose_name = "عنصر طلب"
        verbose_name_plural = "عناصر الطلب"

    def __str__(self):
        return f"{self.quantity} × {self.product.name}"
