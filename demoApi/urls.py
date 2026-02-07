from django.db import router
from django.urls import path,include
from demoApi.views import *
from rest_framework.routers import DefaultRouter


# router = DefaultRouter()
# router.register('trainerSET', TrainerSET, basename='trainerSET') # http://127.0.0.1:8000/demoapi/trainerSET/

# urlpatterns = router.urls





urlpatterns = [
    path('getTrainers/', get_trainers, name='gettrainers'),
    # path('trainerBase/', TrainerAPI.as_view(), name='trainerBase'),
]







