from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    phone = forms.CharField(required=False, label="رقم الجوال")
    address = forms.CharField(required=False, label="العنوان", widget=forms.Textarea)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("username", "email", "phone", "address")
