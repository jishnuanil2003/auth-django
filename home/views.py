from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.db import IntegrityError

# Create your views here.
def home(request):
    return render(request,'Home.html')
def index(request):
    return render(request,'index.html')

def loginn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate (request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render(request,'login.html',{'error':'Invalid username or password'})
    return render(request,'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username already taken'})
        elif User.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error': 'Email already registered'})
        else:
            try:
                User.objects.create_user(username=username, email=email, password=password)
                return redirect('login')  
            except IntegrityError:
                return render(request, 'signup.html', {'error': 'Something went wrong. Please try again.'})

    return render(request, 'signup.html')