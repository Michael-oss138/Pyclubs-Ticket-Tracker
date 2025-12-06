from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            fullname=form.cleaned_data['fullname']
            password=form.cleaned_data['password']

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            user.first_name = fullname
            user.save()

            messages.success(request, "Account has been created successfully")
            return redirect("login")
        
        else:
            messages.error(request, "Please correct the errors below")

    else:
        form = RegisterForm()
    return render(request, "register.html", {"form":form})

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