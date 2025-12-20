from django.shortcuts import render
from SMS.models import *
from django.http import HttpResponse

# Create your views here.


def view_studentRegistration(request):
    if request.method == "GET":
        resp = render(request, 'SMS/studentReg.html')
        return resp
    elif request.method == "POST":
        if 'btnSubmit' in request.POST:
            s1 = student()
            s1.name = request.POST.get('name',"NA")
            s1.age = int(request.POST.get('age',0))
            s1.mobileNo = request.POST.get('mobileNo','NA')
            s1.dob = request.POST.get("dob","NA") or None
            s1.pic = request.FILES.get("pic")
            s1.save()
            resp = HttpResponse("Data Saved Successfully!!")
            return resp
        else:
            resp = render(request, 'SMS/studentReg.html')
            return resp
        
def view_student_wise_paymentDetails(request):
    s1 = student.objects.all()
    d1 = {'students':s1}
    if request.method == "GET":
        
        resp = render(request, "SMS/studentPayment.html",context=d1)
        return resp
    elif request.method == "POST":
        paymentDetails.objects.create(
            amount=request.POST.get("amount"),
            payment_mode=request.POST.get("payment_mode"),
            student_id=request.POST.get("student")
        )
        resp = HttpResponse("Payment Done Successfully!!")
        return resp

def view_student_wise_paymentDetails(request):
    if request.method == "GET":
        resp = render(request,"SMS/paymentDetails.html")
        return resp
    elif request.method == "POST":
        sid = int(request.POST.get("txtID",0))
        # print("--------------------------sid--------------",sid)
        s1 = student.objects.get(id=sid)
        # print(s1)
        allp = s1.paymentdetails_set.all()
        # print("-------------------------------------",allp)
        d1 = {'payments':allp,'stu':s1}
        resp = render(request,"SMS/paymentDetails.html",context=d1)
        return resp
    

def view_courseAdd(request):
    if request.method == "GET":
        c = Course.objects.all()
        s = student.objects.all()
        d1 = {'course':c,'student':s}
        resp = render(request,'SMS/addCourse.html',context=d1)
        return resp
    if request.method == "POST":
        if 'btnAddCourse' in request.POST:
            s_id = request.POST.get('s_id')
            c_id = request.POST.get('c_id')

            if not s_id or not c_id:
                return HttpResponse("<h2 style='color:red'>Please select both Student and Course</h2>")

            try:
                s_obj = student.objects.get(id=s_id)
                c_obj = Course.objects.get(id=c_id)

                c_obj.student.add(s_obj)

                # return HttpResponse("<h1 style='color:green'>Student Added Successfully!</h1>")
                resp = render(request,"SMS/addCourseSuccess.html")
                return resp

            except student.DoesNotExist:
                return HttpResponse("<h2 style='color:red'>Student not found</h2>")

            except Course.DoesNotExist:
                return HttpResponse("<h2 style='color:red'>Course not found</h2>")







            
