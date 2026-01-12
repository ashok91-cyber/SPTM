from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login


@login_required(login_url='/login/')

# Create your views here.
def home(request):
    return render(request,'home.html')

from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(
            request,
            email=email,
            password=password
        )

        if user is not None:
            auth_login(request, user)
            return redirect('/home/')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('/login/')

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # phone=request.POST.get('phone')

        # validations

        

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('/register/')

        # create user
        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Account created successfully")
        return redirect('/login/')

    return render(request, 'register.html')

def profile(request):
    return render(request,'profile.html')

def forgot(request):
    return render(request,'forgot.html')

def manage_task(request):
    return render(request,'manage_task.html')

def logout(request):
    logout(request)
    return redirect('/login/')