from django.shortcuts import render
from rest_framework import viewsets      
from .serializers import RTQASerializer  
from .models import Question              

class RTQAView(viewsets.ModelViewSet):   
    serializer_class = RTQASerializer      
    queryset = Question.objects.all()