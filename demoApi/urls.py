from django.urls import path
from demoApi.views import *


urlpatterns = [
    path('trainers/', get_trainers, name='get_trainers'),
    
]
