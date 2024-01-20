from django.db import models
from apps.models.appTypeModel import AppType


class App(models.Model):
    name = models.CharField(max_length=150)
    type = models.ForeignKey(AppType, on_delete=models.CASCADE)
    version = models.CharField(max_length=255)
    versionCode = models.IntegerField()
    url = models.TextField()
    icon = models.TextField()
    description = models.TextField()
    isPublished = models.BooleanField(False)
    isFree = models.BooleanField(False)
