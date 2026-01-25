from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .decorator import is_CheckinloginorRegister
from django.contrib.auth.decorators import login_required


# Create your views here.

def viewDashboard(request):
    resp = render(request, "LMS/dashboard.html")
    return resp

@is_CheckinloginorRegister
def viewRegister(request):
    if request.method == "GET":
        frm_unbound = UserCreationForm()
        d1 = {"form": frm_unbound} 
        resp = render(request, "LMS/register.html",context=d1)
        return resp
    elif request.method == "POST":
        frm_bound = UserCreationForm(request.POST)
        if frm_bound.is_valid():
            frm_bound.save()
            # resp = HttpResponse("User Registered Successfully")
            resp = render(request, "LMS/register_success.html")
            return resp
        else:
            d1 = {"form": frm_bound} 
            resp = render(request, "LMS/register.html",context=d1)
            return resp
        
@is_CheckinloginorRegister
def viewLogin(request):
    if request.method == "GET": 
        resp = render(request, "LMS/login.html")
        return resp
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password) # it returns User object if credentials are correct else None
        if user is not None:
            login(request, user) # it creates session for the user
            resp = redirect("home")
            return resp
        else:
            resp = render(request, "LMS/login.html", context={"error":"Invalid Credentials"})
            return resp

@login_required(login_url='login')
def viewSecure1(request):
    resp = render(request, "LMS/secure1.html")
    return resp


@login_required(login_url='login')
def viewSecure2(request):
    resp = render(request, "LMS/secure2.html")
    return resp


def viewUnSecure1(request):
    resp = render(request, "LMS/unsecure1.html")
    return resp

def viewUnSecure2(request):
    resp = render(request, "LMS/unsecure2.html")
    return resp

@login_required(login_url='login')
def viewLogout(request):
    logout(request) # it removes the session for the user
    resp = render(request, "LMS/logout.html")
    return resp