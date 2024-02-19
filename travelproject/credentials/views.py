from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages , auth
from django.contrib.auth.models  import User

# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.error
            return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method== 'POST':
        usrname=request.POST['username']
        frstname=request.POST['First_name']
        last_name=request.POST['Last_name']
        email=request.POST['email']
        passwrd=request.POST['password']
        cpasswrd=request.POST['password1']
        if passwrd==cpasswrd:
            if User.objects.filter(username=usrname).exists():
                messages.info(request,"Username Taken")
                return redirect('register')
            
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already Taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=usrname,password=passwrd,first_name=frstname,last_name=last_name,email=email)

            
                user.save();
                return redirect('login')   
            
        else:
            messages.info(request,"password not match")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")