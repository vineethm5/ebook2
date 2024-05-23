from django.urls import path
from .views import *
urlpatterns=[
    path("",home,name='home'),
    path("login/",login,name='login'),
    path("register/",register,name='register'),
    path("addBook1/<int:userid>/",addBook1,name='addBook'),
    # path('addBook1/',addBook,name='addbook'),
    path("logout/",logout,name='logout'),
    path("contri/<int:id>",contri,name='contri'),
    
    
]