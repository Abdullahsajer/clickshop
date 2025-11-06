from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm

User = get_user_model()

def login_view(request):
    if request.method == 'POST':
        identifier = request.POST['identifier']
        password = request.POST['password']

        try:
            if '@' in identifier:
                user = User.objects.get(email__iexact=identifier)
                username = user.username
            else:
                username = identifier
        except User.DoesNotExist:
            username = identifier

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')

        return render(request, 'accounts-templates/login.html', {
            'error': 'بيانات تسجيل الدخول غير صحيحة'
        })

    return render(request, 'accounts-templates/login.html')


def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = CustomUserCreationForm()
    return render(request, "accounts-templates/register.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect('login')
