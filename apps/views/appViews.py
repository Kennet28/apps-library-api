from rest_framework import generics

from apps.models.appModel import App
from apps.serializers.appSerializer import AppSerializer


# Create your views here.



class AppList(generics.ListAPIView):
    queryset = App.objects.all()
    serializer_class = AppSerializer


class AppCreate(generics.CreateAPIView):
    queryset = App.objects.all()
    serializer_class = AppSerializer


class AppUpdate(generics.UpdateAPIView):
    queryset = App.objects.all()
    serializer_class = AppSerializer
