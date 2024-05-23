from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from myapp.forms import ebookforms
from myapp.models import ebookss
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
# def addBook(req,userid=None):
#     if id is not None:
#         user = get_object_or_404(User, id=id)
#     else:
#         user = None  # Handle case where no user id is provided

#     if req.method == 'POST':
#         form = ebookforms(req.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')  # Redirect to a success page or home page
#     else:
#         form = ebookforms()
#     return render(req,"addBook.html",{'user':userid,'forms':form})

def addBook(request, id=None):
    print("hi")
    if id is not None:
        user = get_object_or_404(User, id=id)
    else:
        user = None

    if request.method == 'POST':
        form = ebookforms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Ensure 'home' is the correct name for your success URL
    else:
        form = ebookforms()

    return render(request, 'addBook.html', {'form': form, 'user': user})

def logout(req):
    auth.logout(req)
    return redirect("/")

def contri(req,userid):
    pass

def addBook(req,userid):
    pass 