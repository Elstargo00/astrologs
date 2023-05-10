from django.shortcuts import render
from zodioscope.models import ZodioscopeDaily
from rest_framework import generics
from .serializers import ZodioscopeDailySerializer

# Create your views here.

class ZodioscopeDailyAPIView(generics.ListAPIView):
    queryset = ZodioscopeDaily.objects.all()
    serializer_class = ZodioscopeDailySerializer

class DetailZodioscopeDailyAPIView(generics.RetrieveAPIView):
    queryset = ZodioscopeDaily.objects.all()
    serializer_class = ZodioscopeDailySerializer