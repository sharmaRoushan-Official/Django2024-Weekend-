from django.urls import path
# from EMS.views import viewHome
from .views import *    


urlpatterns = [
    path('home/',viewHome),  # 127.0.0.1:8000/EMS/home/
    path('index/',viewIndex),  # 127.0.0.1:8000/EMS/index/
    path('calculator/',viewCalculator), # 127.0.0.1:8000/EMS/calculator/
    # path('practice/',viewPractice),  # 127.0.0.1:8000/EMS/practice/
    # path('practice2/',viewPractice2),
    path('practice/',viewPractice),
    # path('employee/',viewEmployee),
    path('dummyEmp/',viewDummyEmployee),
]
