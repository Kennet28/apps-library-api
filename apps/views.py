from django.shortcuts import render
from rest_framework import generics

from apps.models import AppType, App
from apps.serializers import AppTypeSerializer, AppSerializer


# Create your views here.
class AppTypesList(generics.ListAPIView):
    queryset = AppType.objects.all()
    serializer_class = AppTypeSerializer


class AppList(generics.ListAPIView):
    queryset = App.objects.all()
    serializer_class = AppSerializer


class AppCreate(generics.CreateAPIView):
    queryset = App.objects.all()
    serializer_class = AppSerializer


class AppUpdate(generics.UpdateAPIView):
    queryset = App.objects.all()
    serializer_class = AppSerializer
