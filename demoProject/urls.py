"""
URL configuration for demoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse
from django.shortcuts import render


# def viewHello(request):
#     resp = HttpResponse("<h1>Hello world</h1>")
#     return resp
    
# # write a code to sum of two numbers.

# def viewSum(request,a,b):
#     resp = HttpResponse("<h1>The sum of two numbers is:"+str(a+b)+"</h1>")
#     return resp

# # subtract
# def viewSub(request,a,b):
#     resp = HttpResponse("<h1>The subtract of two numbers is:"+ str(a-b)+ "</h1>")
#     return resp

# # multiply
# def viewMulti(request,a,b):
#     resp = HttpResponse("<h1>The Multiplication of two numbers is:"+str(a*b)+"</h1>")
#     return resp

# # division

# def viewDiv(request,a,b):
#     resp = HttpResponse("<h1>The Division of two numebrs is:"+str(a/b)+"</h1>")
#     return resp

# # modulus
# def viewMod(request,a,b):
#     resp = HttpResponse("<h1>The Reminder of the value is:"+str(a%b)+"</h1>")
#     return resp


# # Exponent

# def viewExpo(request,a,b):
#     resp = HttpResponse("<h1>The Exponent of the two value is:"+str(a**b)+"</h1>")
#     return resp

# GET Method
# def viewCalc(request):
#     a = int(request.GET.get('txtFirst',"NA"))
#     print("-----------------a------------",a,type(a))
#     b = int(request.GET.get('txtSecond',"NA"))
#     print("---------------b------------",b,type(b))
#     c = int(request.GET.get("txtThird","NA"))
#     print('---------------c-----------',c,type(c))

#     # sum on the terminal
#     sum1 = a+b+c
#     print("Sum of the value is:",sum1)
#     resp = render(request,"calc.html")
#     return resp


# post method
def viewCalc(request):
    a = int(request.POST.get('txtFirst',0))
    b = int(request.POST.get('txtSecond',0))
    sum1 = a+b
    # print("sum of the value is:",sum1)

    d1 = {'a':a,'b':b,'sum':sum1}
    resp = render(request,"calc.html",context=d1)
    return resp


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home/',viewHello),
    # path('sum/<int:a>/<int:b>/',viewSum),
    # path('sub/<int:a>/<int:b>/',viewSub),
    # path('multi/<int:a>/<int:b>/',viewMulti),
    # path('divide/<int:a>/<int:b>/',viewDiv),
    # path('rem/<int:a>/<int:b>/',viewMod),
    # path('expo/<int:a>/<int:b>/',viewExpo),
    path('calc/',viewCalc),
    path('EMS/',include("EMS.urls")), # 127.0.0.1:8000/EMS/
    path('SMS/',include("SMS.urls")), # http://127.0.0.1:8000/SMS/ 
]
