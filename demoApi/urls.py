from django.db import router
from django.urls import path,include
from demoApi.views import *
from rest_framework.routers import DefaultRouter


# router = DefaultRouter()
# router.register('trainerSET', TrainerSET, basename='trainerSET') # http://127.0.0.1:8000/demoapi/trainerSET/

# urlpatterns = router.urls





urlpatterns = [
    path('getTrainers/', get_trainers, name='gettrainers'),
    path('deleteTrainer/<int:trainer_id>/', delete_trainer, name='deletetrainer'),
    # path('trainerBase/', TrainerAPI.as_view(), name='trainerBase'),

    path('getEmployees/', get_employees, name='getemployees'),
    path('postEmployees/', post_employees, name='postemployees'),
]







