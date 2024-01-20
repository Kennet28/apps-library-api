from rest_framework import serializers

from apps.models.appTypeModel import AppType


class AppTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppType
        fields = '__all__'


