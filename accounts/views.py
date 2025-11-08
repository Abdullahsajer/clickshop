from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm

User = get_user_model()

def login_view(request):
    if request.method == 'POST':
        identifier = request.POST.get('identifier')
        password = request.POST.get('password')

        user = None
        if identifier and password:
            # Try authenticating directly with the identifier as username
            user = authenticate(request, username=identifier, password=password)

            # If direct username authentication failed, try authenticating by email
            if not user and '@' in identifier:
                try:
                    # Find user by email
                    user_by_email = User.objects.get(email__iexact=identifier)
                    # Authenticate using the found user's username
                    user = authenticate(request, username=user_by_email.username, password=password)
                except User.DoesNotExist:
                    pass # Email not found, user remains None

        if user:
            login(request, user)
            return redirect('home')
        else:
            # Authentication failed
            return render(request, 'accounts-templates/login.html', {
                'error': 'بيانات تسجيل الدخول غير صحيحة',
                'identifier': identifier # Keep identifier in form for user convenience
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
    return redirect('accounts:login')
