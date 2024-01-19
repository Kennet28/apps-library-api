from rest_framework import serializers

from apps.models import AppType, App


class AppTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppType
        fields = '__all__'


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = '__all__'
