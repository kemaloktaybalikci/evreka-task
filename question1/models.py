from django.db import models
from django.db.models.aggregates import Count
from random import randint
class VehicleManager(models.Manager):
    def random(self):
        count = self.aggregate(count=Count('pk'))['count']
        random_index = randint(0, count - 1)
        return self.all()[random_index]

class Vehicle(models.Model):
    plate = models.CharField(max_length=200)
    objects = VehicleManager() 
    def __str__(self):
        return self.plate

class NavigationRecord(models.Model):
    def __str__(self):
        return str(self.id) + "-" + self.vehicle.plate
    datetime =models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    vehicle = models.ForeignKey(Vehicle,on_delete=models.CASCADE)



    

