from django.urls import path 
from LMS.views import *


urlpatterns = [
    path("home/",viewDashboard,name="home"),
    path("login/",viewLogin,name="login"),
    path("secure1/",viewSecure1,name="secure1"),
    path("secure2/",viewSecure2,name="secure2"),
    path("unsecure1/",viewUnSecure1,name="unsecure1"),
    path("unsecure2/",viewUnSecure2,name="unsecure2"),
    
]
