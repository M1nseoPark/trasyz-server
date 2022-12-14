from django.db import models

# Create your models here.
class Parkinglot(models.Model):
    pid = models.IntegerField()
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=500)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    kickboard = models.IntegerField()
    bicycle = models.IntegerField()

class Run(models.Model):
    rid = models.CharField(max_length=50)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
