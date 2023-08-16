from django.shortcuts import render
from rest_framework.decorators import api_view,  permission_classes
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework import status
from .serializers import  WorkerSerializer

from .models import BasicInfo, ContactInfo, EmerContactInfo, Worker

class WorkerView():

    # @api_view(['POST'])
    # @permission_classes([IsAuthenticated])
    def workerCreate(request):
        worker = request.data
        workerSerializer = WorkerSerializer(data=worker)
        workerSerializer.is_valid(rais_exception=True)
        workerSerializer.save()
        return Response(workerSerializer.data)
    
    @api_view(['GET'])
    @permission_classes([IsAuthenticated])
    def workerGet(request):
        workers = Worker.objects.all()
        workerSerializer = WorkerSerializer(workers, many=True)
        return JsonResponse(workerSerializer, safe=False)
