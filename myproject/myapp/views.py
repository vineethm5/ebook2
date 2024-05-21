from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(req):
    return render(req,"home.html")

def login(req):
    if req.method == "POST":
        name=req.POST.get("username")
        password=req.POST.get("password")
        if not User.objects.filter(username=name).exists():
            messages.info(req,"User Doesn't exits")
        else:
            user=authenticate(username=name,password=password)
            if user is None:
                messages.info(req,"Please enter valid password")
            else:
                auth.login(req,user)
                return render(req,"home.html")

    return render(req,"login.html")              

def register(req):
    if req.method == "POST":
        name=req.POST.get('username')
        email=req.POST.get("email")
        password=req.POST.get("password")
        user=User.objects.filter(username=name)
        if user.exists():
            messages.info(req,"User Alredy Exists")
            redirect("/register.html")
        else:    
            user= User.objects.create_user(
                username=name,
                email=email
            )
            user.set_password(password)
            user.save()
            messages.info(req,"Signedup Succussfully")

    return render(req,"register.html")

@login_required
def addBook(req,user_id):
    # user=User.objects.get(id=user_id)
    return render(req,"addBook.html")

def logout(req):
    auth.logout(req)
    return redirect("/")

def contri(req,userid):
    pass

def addBook(req,userid):
    pass