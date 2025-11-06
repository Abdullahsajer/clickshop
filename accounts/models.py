from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="رقم الجوال")
    address = models.TextField(blank=True, null=True, verbose_name="العنوان")

    class Meta:
        verbose_name = "مستخدم"
        verbose_name_plural = "مستخدمون"

    def __str__(self):
        return f"{self.username} - {self.email}"
