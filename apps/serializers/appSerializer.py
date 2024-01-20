from rest_framework import serializers

from apps.models.appModel import App
from apps.models.appTypeModel import AppType


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = '__all__'
