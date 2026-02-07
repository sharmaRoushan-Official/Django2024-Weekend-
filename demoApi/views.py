from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from demoApi.models import Trainer
from demoApi.serialize import TrainerSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet


# Create your views here.
@api_view(['GET','POST','PATCH'])
def get_trainers(request):
    if request.method == 'GET':
        trainer = Trainer.objects.all()
        serializer = TrainerSerializer(trainer, many=True) # Convert to JSON
        return Response(serializer.data,status=status.HTTP_200_OK) # Return JSON response with status 200 OK
    
    if request.method == 'POST':
        serializer = TrainerSerializer(data=request.data) # Deserialize JSON data from request
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PATCH':
        trainer_id = request.data.get('id')
        try:
            trainer = Trainer.objects.get(id=trainer_id)
        except Trainer.DoesNotExist:
            return Response({'error': 'Trainer not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = TrainerSerializer(trainer, data=request.data, partial=True) # Allow partial update
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# CBV [class based view]
# class TrainerAPI(APIView):
#     def get(self,request):
#         trainers = Trainer.objects.all()
#         serializer = TrainerSerializer(trainers, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


# class TrainerSET(ModelViewSet):
#     queryset = Trainer.objects.all()
#     serializer_class = TrainerSerializer
#     http_method_names = ['get', 'post', 'put', 'patch', 'delete'] # Allow all HTTP methods for this viewset



