from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms

# استدعاء موديل المستخدم المخصص
User = get_user_model()

# نموذج تسجيل مستخدم جديد
class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="كلمة المرور")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="تأكيد كلمة المرور")

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'address', 'password']

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("password") != cleaned_data.get("confirm_password"):
            raise forms.ValidationError("كلمتا المرور غير متطابقتين.")
        return cleaned_data


# فيو إنشاء حساب
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('accounts:login')
    else:
        form = RegisterForm()
    return render(request, 'accounts-templates/register.html', {'form': form})


# فيو تسجيل الدخول
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('/')  # توجيه للصفحة الرئيسية بعد تسجيل الدخول
    else:
        form = AuthenticationForm()

    return render(request, 'accounts-templates/login.html', {'form': form})
