from django.shortcuts import render
from rest_framework.decorators import api_view,  permission_classes
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


