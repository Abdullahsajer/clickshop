from django import forms
from django.contrib.auth import get_user_model
from .models import Order

User = get_user_model()

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name', 'address', 'phone', 'city']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'الاسم الكامل'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'العنوان'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'رقم الجوال'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'المدينة'}),
        }
        labels = {
            'full_name': 'الاسم الكامل',
            'address': 'العنوان',
            'phone': 'رقم الجوال',
            'city': 'المدينة',
        }
