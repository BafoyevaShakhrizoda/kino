from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get['username']
        password = request.POST.get['password']
        users = authenticate(request, username = username , password = password)
        if users is not None:
            login(request,users)
            return redirect(reverse('home.html'))
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password1)
        login(request, user)
        return redirect('home')  
    return render(request, 'register.html')
