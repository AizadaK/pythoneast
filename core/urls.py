from django.urls import path 
from .views import *

urlpatterns = [
    path("", homepage, name="home"),
    path("singin", authorization, name="login"),
    path("singout/", singout, name="logout"),
    path("registration/", registration, name="registration")
    
]