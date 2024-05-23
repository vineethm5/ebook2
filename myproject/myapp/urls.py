from django.urls import path
from .views import *
urlpatterns=[
    path("",home,name='home'),
    path("login/",login,name='login'),
    path("register/",register,name='register'),
    path("addBook/<int:userid>/",addBook,name='addBook'),
    path('addBook/',addBook,name='addbook'),
    path("logout/",logout,name='logout'),
    path("contri/<int:id>",contri,name='contri'),
    
    
]