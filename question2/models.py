from django.db import models

class Bin(models.Model):
    def __str__(self):
        return str(self.id)
    latitude = models.FloatField()
    longitude = models.FloatField()   

class Operation(models.Model):
    def __str__(self):
        return self.name
    name=models.CharField(max_length=200)

class Collection(models.Model):
    bin = models.ForeignKey(Bin,null=True,on_delete=models.SET_NULL)
    operation = models.ForeignKey(Operation,null=True,on_delete=models.SET_NULL)
    collection_frequency=models.IntegerField()
    last_collection=models.DateTimeField()



    

