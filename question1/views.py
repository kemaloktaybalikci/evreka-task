from this import s
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import VehicleSerializer,NavigationRecordsSerializer
from django.core.serializers import serialize
from django.shortcuts import render
from .utils.fakeData import FakeDataGenerator
from django.db import transaction
from .models import NavigationRecord, Vehicle
from datetime import datetime, timedelta



# Create your views here.
class VehicleListView(APIView):
    def get(self, request):
        vehicles = Vehicle.objects.filter().all()
        serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class VehicleDetailView(APIView):
    def get(self, request,vehicle_id):
        vehicle = Vehicle.objects.get(id=vehicle_id)
        serializer = VehicleSerializer(vehicle, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

class VehicleNavigationRecordsView(APIView):
    def get(self, request,vehicle_id):
        vehicle = Vehicle.objects.get(id=vehicle_id)
        endDateTime =  datetime.now()
        startDateTime = endDateTime - timedelta(hours=4000)
        navigationRecords= NavigationRecord.objects.filter(datetime__range=[startDateTime, endDateTime],vehicle=vehicle)

        serializer = NavigationRecordsSerializer(navigationRecords, many=True)
        return Response({"last_points":serializer.data}, status=status.HTTP_200_OK)

class CreateDummyVehiclesView(APIView):
    def get(self, request,record_num):
        fake_vehicles=FakeDataGenerator.make_vehicles(record_num)
        for vehicle in fake_vehicles:
            with transaction.atomic():
                new_vehicle = Vehicle.objects.create(plate=vehicle['plate'])
                new_vehicle.save()
        return Response({"Message":"Vehicles are created succesfully","Vehicles":fake_vehicles}, status=status.HTTP_200_OK)

class CreateDummyNavigationRecordsView(APIView):
    def get(self, request,record_num):
        fake_navigation_records= FakeDataGenerator.make_navigation_records(record_num)
        for record in fake_navigation_records:
            with transaction.atomic():
                new_navigation_record = NavigationRecord.objects.create(datetime=record['datetime'],latitude=record['latitude'],longitude=record['longitude'],vehicle=record['vehicle'])
                new_navigation_record.save()
        return Response({"Message":"Records are created succesfully"}, status=status.HTTP_200_OK)
