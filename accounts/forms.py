from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    phone = forms.CharField(required=False, label="رقم الجوال (اختياري)")
    address = forms.CharField(required=False, widget=forms.Textarea, label="العنوان (اختياري)")

    class Meta:
        model = CustomUser
        fields = ("username", "email", "phone", "address", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "input-field"})
