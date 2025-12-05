from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exosts")
            return redirect("register")

        user = User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, "Account created successfully")
        return redirect("login")
    return render(request, "register.html")

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, "Incorrect Credentials")
            return redirect("login")
        login(request, user)
        return redirect("event_list")
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect("login")