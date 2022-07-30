import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin

class Vehicle(models.Model):
    plate = models.CharField(max_length=200)
    def __str__(self):
        return self.plate

class NavigationRecord(models.Model):
    datetime = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    vehicle = models.ForeignKey(Vehicle,on_delete=models.CASCADE)



