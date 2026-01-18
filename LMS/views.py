from django.shortcuts import render

# Create your views here.

def viewDashboard(request):
    resp = render(request, "LMS/dashboard.html")
    return resp


def viewLogin(request):
    resp = render(request, "LMS/login.html")
    return resp

def viewSecure1(request):
    resp = render(request, "LMS/secure1.html")
    return resp


def viewSecure2(request):
    resp = render(request, "LMS/secure2.html")
    return resp


def viewUnSecure1(request):
    resp = render(request, "LMS/unsecure1.html")
    return resp

def viewUnSecure2(request):
    resp = render(request, "LMS/unsecure2.html")
    return resp