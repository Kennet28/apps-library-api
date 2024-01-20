from rest_framework import generics

from apps.models.appModel import AppType
from apps.serializers.appTypeSerializer import AppTypeSerializer


class AppTypesList(generics.ListAPIView):
    queryset = AppType.objects.all()
    serializer_class = AppTypeSerializer
