from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Employee
from .serializers import EmpSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class EmpViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmpSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]



