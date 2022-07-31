from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.urls import reverse
from django.core.serializers import serialize
from django.shortcuts import render
from .utils.fakeData import FakeDataGenerator
from django.db import transaction
from .models import NavigationRecord, Vehicle
from datetime import datetime, timedelta
from django.db.models import F, Func, Value, CharField


# Create your views here.
def index(request):
    vehicles=Vehicle.objects.all()
    NavigationRecords=NavigationRecord.objects.all()

    return render(request,'question1/index.html',{'vehicles':vehicles,'navigationRecords':NavigationRecords})



def basicSolution(request,vehicle_id):

    vehicle= Vehicle.objects.get(pk=vehicle_id)
    endDateTime =  datetime.now()
    startDateTime = endDateTime - timedelta(hours=4000)
    last_points= NavigationRecord.objects.filter(datetime__range=[startDateTime, endDateTime],vehicle=vehicle).select_related('vehicles').annotate(
        vehicle_plate=F('vehicle__plate'),
        formatted_date=Func(F(datetime.now()),function='TRUNC'
  )
        )
    fields=["longitude","latitude","datetime","vehicle_plate","formatted_date"]
    last_points_data= list(last_points.values(*fields))
    #last_points_json = serializers.serialize('json', last_points)
    return render(request,'question1/index.html',{'vehicles':vehicle,'navigationRecords':last_points_data})

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

