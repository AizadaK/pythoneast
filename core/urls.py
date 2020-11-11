from django.urls import path 
from .views import *

urlpatterns = [
    path("", homepage, name="home"),
    path("singin", authorization, name="login"),
    
]