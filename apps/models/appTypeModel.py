from django.db import models


class AppType(models.Model):
    name = models.CharField(max_length=150)

