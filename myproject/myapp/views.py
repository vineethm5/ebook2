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
def addBook1(request,userid=None):
    if request.method == 'POST':
        form = ebookforms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Ensure 'home' is the correct name for your success URL
    else:
        form = ebookforms()

    return render(request, 'addBook.html',{'userr':userid,'formm':form})

def exploree(req):
    educationalbook=ebookss.objects.filter(category='Education')
    fictiona=ebookss.objects.filter(category='Fiction')
    science=ebookss.objects.filter(category='Science')
    return render(req,"explore.html",{'education':educationalbook,"fiction":fictiona,"science":science})

def logout(req):
    auth.logout(req)
    return redirect("/")

def contri(req,bid):
    ebookcon=ebookss.objects.filter(id=bid)
    return render(req,"contri.html",{'books':ebookcon})

def viewbooks(req,bid):
    ebookd=ebookss.objects.get(id=bid)
    return render(req,"viewBook.html",{'book':ebookd})

def deleteBook(req,bid):
    book=ebookss.objects.get(id=bid)
    book.delete()
    return redirect("/")

def editBooks(req,bid):
    book=ebookss.objects.get(id=bid)
    if req.method == 'POST':
        #When you want to update an existing object, you retrieve the object from the database and pass it to the form as an instance. This pre-fills the form with the existing data and allows the user to edit it.
        form=ebookforms(req.POST,req.FILES,instance=book)
        if form.is_valid():
            form.save()
            print()
            print("book updated succesfully")
        else:
            print(form.errors)
    else:
        form=ebookforms(instance=book)
    return render(req,"editbook.html",{'form':form})

    