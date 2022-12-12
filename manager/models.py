from django.db import models

# Create your models here.
class Parkinglot(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=500)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    kickboard = models.IntegerField()
    bicycle = models.IntegerField()


