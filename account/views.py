from email import message
from django.shortcuts import render , redirect
from django.contrib import messages ,auth
from django.contrib.auth.models import User

# Create your views here.


def register(request):

    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request , "User already exists")
                return redirect('account:register')
            elif User.objects.filter(email=email):
                messages.error(request , "Email already taken")
                return redirect('account:register')
            else:
                user = User.objects.create_user(first_name=firstname , last_name=lastname, username=username, email=email, password=password)
                auth.login(request , user)
                messages.success(request , "You are Now Logged In")
                return redirect('meals:home')    
                   
         
        else:
            messages.error(request , 'Password do not match')
            return redirect('account:register') 
    else:
        return render(request , 'account/register.html')        


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username , password=password)
        if user is not  None:
            messages.success(request , "You are now successfylly logged In")
            auth.login(request , user)
            return redirect('meals:home')
        else:
            messages.error(request , "Login Failed!")
            return redirect('account:login')    
    else:
        return render(request , 'account/login.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        
        messages.success(request , "YOU ARE LOGGED OUT!")
        return redirect("meals:home")
    print("TETS")    
    return redirect('meals:home')    
