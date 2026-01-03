from django.urls import path
from .views import *



urlpatterns = [
    path('stuReg/',view_studentRegistration), #http://127.0.0.1:8000/SMS/stuReg/
    path('studentPay/',view_student_wise_paymentDetails), #http://127.0.0.1:8000/SMS/studentPay/
    path('payDetails/',view_student_wise_paymentDetails), #http://127.0.0.1:8000/SMS/payDetails/
    path('addCourse/',view_courseAdd,name="addCourse"),
    path('addPayment/',viewAddPayment,name="addPayment"),
    path('stuFrm/',view_student_frm,name="stuFrm"),
]
