from django.shortcuts import render
from django.http import HttpResponse
from EMS.models import Employee


# Create your views here.


def viewHome(request):
    resp = HttpResponse("<h1>Hello Vaishnavi!! This is calling application view</h1>")
    return resp


def viewIndex(request):
    resp = render(request,"EMS/index.html")
    return resp

def viewCalculator(request):
    num1 = int(request.POST.get("num1",0))
    num2 = int(request.POST.get("num2",0))

    if request.method == "GET":
        resp = render(request,"EMS/calculator.html")
        return resp
    elif request.method == "POST":
        if 'btnSum' in request.POST:
            c = num1+num2 
            # print("-------------c---------------",c)
        elif 'btnSub' in request.POST:
            c = num1-num2
        d1 = {"num1":num1,"num2":num2,'sum1':c}
    resp = render(request,"EMS/calculator.html", context=d1)
    return resp

# 1.WAP to check the number is equal to 100 or not.
# def viewPractice(request):
#     d1 = {'a':101}
#     resp = render(request,"EMS/practiceDTL.html",context=d1)
#     return resp


# 2.Write to check smallest in two numbers. 
# def viewPractice(request):
#     d1 = {'a':200,'b':100}
#     resp = render(request,"EMS/practiceDTL.html",context=d1)
#     return resp


# def viewPractice(request):
#     d1 = {'a':99,'b':100, 'c':105}
#     resp = render(request,"EMS/practiceDTL.html",context=d1)
#     return resp


# def viewPractice2(request):
#     num1 = int(request.POST.get("num1",0))
#     num2 = int(request.POST.get('num2',0))
#     # print("---------------num----------",num1)
#     # print('---------------num2----------',num2)
#     d1 = {'num1':num1,'num2':num2}
#     resp = render(request,"EMS/practice2.html",context=d1)
#     return resp


# def viewPractice(request):
#     d1 = {'val':101}
#     resp = render(request,"EMS/practiceDTL2.html",context=d1)
#     return resp

# def viewPractice(request):
#     d1 = {'a':1005,'b':105}
#     resp = render(request,'EMS/practiceDTL2.html',context=d1)
#     return resp


def viewPractice(request):
    d1 = {'a': 550, 'b': 100, 'c':205}
    resp = render(request, 'EMS/practiceDTL2.html',context=d1)
    return resp


# class Employee:
#     def __init__(self):
#         self.name = ""
#         self.age = 0
#         self.address = ""
#         self.mobileno = ""
#         self.post = ""
#         self.salary = 0

# def get_N_Employee(n):
#     empList = []
#     for i in range(1,n+1):
#         emp = Employee()
#         emp.name = "Flix" + str(i)
#         emp.age = 23 + i
#         emp.address = "Ashok Nagar" + str(i)
#         emp.mobileno = "35615644" + str(i)
#         emp.post = "SE" + str(i)
#         emp.salary = 454545 + i
#         empList.append(emp)
#     return empList

# def viewEmployee(request):
#     if request.method == "GET":
#         resp = render(request,"EMS/home.html")
#         return resp
#     elif request.method == "POST":
#         empno = int(request.POST.get("txtNo",0))
    
#         employees = get_N_Employee(empno)
#         # print('Employee=',employees)
#         # for emp in employees:
#         #     print(emp.name, emp.age, emp.address, emp.mobileno, emp.post, emp.salary)
#         d1 = {'employees':employees, "empNo":empno}
#         resp = render(request,"EMS/home.html", context=d1)
#         return resp
    

def viewDummyEmployee(request):
    if request.method == "GET":
        resp = render(request,'EMS/insertEmployee.html')
        return resp
    elif request.method == "POST":
        if 'btnAdd' in request.POST:
            emp = Employee()
            emp.name = request.POST.get("txtName","NA")
            emp.age = request.POST.get("txtAg",0)
            emp.mobileno = request.POST.get("txtMobile","NA")
            emp.address = request.POST.get("txtAddress","NA")
            emp.save()
            resp = HttpResponse("<h1>Employee Inserted Successfully!!</h1>")
            return resp
        elif 'btnSearch' in request.POST:
            eid = int(request.POST.get("txtID",0))
            # print(eid)
            emp = Employee.objects.get(id=eid)
            # print(emp)
            d1 = {'emp':emp}
            resp = render(request,'EMS/insertEmployee.html',context=d1)
            return resp
        elif 'btnUpdate' in request.POST:
            emp = Employee()
            emp.id = int(request.POST.get("txtID",0))
            if Employee.objects.filter(id=emp.id).exists():
                emp.name = request.POST.get('txtName','NA')
                emp.age = request.POST.get("txtAge",'NA')
                emp.mobileno= request.POST.get("txtMobile",'NA')
                emp.address = request.POST.get("txtAddress","NA")
                emp.save()
                resp = HttpResponse("<h1>Record Updated Successfully!!</h1>")
                return resp
        elif 'btnDelete' in request.POST:
            emp = Employee()
            emp.id = int(request.POST.get('txtID',0))
            Employee.objects.filter(id=emp.id).delete()
            resp = HttpResponse("<h1>Employee Deleted Successully</h1>")
            return resp
        elif 'btnshowAll' in request.POST:
            allemp = Employee.objects.all()

            d1 = {'employees':allemp}
            resp = render(request,'EMS/insertEmployee.html',context=d1)
            return resp
        









