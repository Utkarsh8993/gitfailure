from django.shortcuts import render , redirect

# Create your views here.
from django.contrib.auth import get_user_model , login,logout,authenticate
from .forms import RegisterForm
from django.contrib import messages

User = get_user_model()


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request , user)
            messages.success(request , "You Were Registered Succesfully")
            return redirect('home')
        else:
            messages.success(request , "Invalid Registration Forn")
            return redirect('register')

    form = RegisterForm()
    return render(request , "users/register.html" , {
        "form" : form
    })



def logout_view(request):
    logout(request)
    messages.success(request , "You have logged out successfully.")                        
    return redirect('home')


def login_view(request):
    if request.method=="POST":
        email=request.POST["email"]
        password=request.POST["password"]
        user=authenticate(email=email, password=password)
        if user is not None:   
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, "There was trouble signing you")
            return redirect('login')

    
    return render(request , "users/login.html")


def user(request , user_id):
    user = User.objects.get(pk=user_id)
    return render(request , "users/user.html" , {
        "user" : user
    })