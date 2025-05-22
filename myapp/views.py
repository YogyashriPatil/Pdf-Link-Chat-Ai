from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('home')  # Replace 'home' with your desired redirect
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'signin.html')


# Sign-up view
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, password=password)
        messages.success(request, 'Account created successfully!')
        return redirect('signin')  # or wherever you want to redirect
    return render(request, 'signup.html')

def home(request):
    return render(request, 'home.html')