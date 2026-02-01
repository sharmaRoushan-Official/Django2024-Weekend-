from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from demoApi.models import Trainer
from demoApi.serialize import TrainerSerializer
from rest_framework import status


# Create your views here.
@api_view(['GET'])
def get_trainers(request):
    trainer = Trainer.objects.all()
    serializer = TrainerSerializer(trainer, many=True) # Convert to JSON
    return Response(serializer.data,status=status.HTTP_200_OK) # Return JSON response with status 200 OK

