from datetime import datetime
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .utils.fakeData import FakeDataGenerator
from django.db import transaction
from .models import NavigationRecord, Vehicle

# Create your views here.
def index(request):
    vehicles=Vehicle.objects.all()
    NavigationRecords=NavigationRecord.objects.all()

    return render(request,'question1/index.html',{'vehicles':vehicles,'navigationRecords':NavigationRecords})


def createDummyVehicles(request,record_num):
    fake_vehicles=FakeDataGenerator.make_vehicles(record_num)
    for vehicle in fake_vehicles:
        with transaction.atomic():
            new_vehicle = Vehicle.objects.create(plate=vehicle['plate'])
            new_vehicle.save()
    return HttpResponseRedirect(reverse('question1:index',))

def createDummyNavigationRecords(request,record_num):
    fake_navigation_records= FakeDataGenerator.make_navigation_records(record_num)
    #return render(request,'question1/index.html',{'navigationRecords':fake_navigation_records})
    for record in fake_navigation_records:
        with transaction.atomic():
            new_navigation_record = NavigationRecord.objects.create(datetime=record['datetime'],latitude=record['latitude'],longitude=record['longitude'],vehicle=record['vehicle'])
            new_navigation_record.save()
    return HttpResponseRedirect(reverse('question1:index',))

