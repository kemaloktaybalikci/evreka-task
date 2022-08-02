from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import VehicleSerializer,NavigationRecordsSerializer,LastPointSerializer
from .utils.fakeData import FakeDataGenerator
from django.db import transaction
from .models import NavigationRecord, Vehicle
from datetime import datetime, timedelta
from django.db.models.aggregates import Max
from django.db.models import F,Subquery,OuterRef


# Create your views here.
class VehicleListView(APIView):
    def get(self, request):
        try:          
            vehicles = Vehicle.objects.filter().all()
            serializer = VehicleSerializer(vehicles, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK,)
        except:
            raise Exception("Something weng wrong")
class VehicleDetailView(APIView):
    def get(self, request,vehicle_id):
        try:
            vehicle = Vehicle.objects.get(id=vehicle_id)
            serializer = VehicleSerializer(vehicle, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            raise Exception("Something weng wrong")
            
class VehicleNavigationRecordsView(APIView):
    def get(self, request):
        try:
            hour_before=48
            endDateTime =  datetime.now()
            startDateTime = endDateTime - timedelta(hours=hour_before)
            ###############    WARNING! - This is a walkaround solution
            ##########    Bug:  Navigations records are filtered by 'datetime'. There is a possibility that some records can have same 'datetime' value. 
            #######       Solution: Find a way to filter records by 'plate' and 'datetime' as pair. 
            vehicle= Vehicle.objects.filter(navigationrecord__datetime__range=[startDateTime,endDateTime]).values('plate').annotate(
                last_datetime=Max('navigationrecord__datetime')).values('last_datetime')
            records=NavigationRecord.objects.filter(datetime__in=vehicle).annotate(
                vehicle_plate=F('vehicle__plate')).order_by('vehicle_id')
            serializer = LastPointSerializer(records, many=True)
            return Response({"last_points":serializer.data}, status=status.HTTP_200_OK)
        except:
            raise Exception("Something weng wrong")

class CreateDummyVehiclesView(APIView):
    def get(self, request,record_num):
        try:
            # Record_num can be limited to prevent crash

            fake_vehicles=FakeDataGenerator.make_vehicles(record_num)
            for vehicle in fake_vehicles:
                with transaction.atomic():
                    new_vehicle = Vehicle.objects.create(plate=vehicle['plate'])
                    new_vehicle.save()
            return Response({"Message":"Vehicles are created succesfully","Vehicles":fake_vehicles}, status=status.HTTP_200_OK)
        except:
            raise Exception("Something weng wrong")

class CreateDummyNavigationRecordsView(APIView):
    def get(self, request,record_num):
        try:
            # Record_num can be limited to prevent crash
    
            fake_navigation_records= FakeDataGenerator.make_navigation_records(record_num)
            for record in fake_navigation_records:
                with transaction.atomic():
                    new_navigation_record = NavigationRecord.objects.create(datetime=record['datetime'],latitude=record['latitude'],longitude=record['longitude'],vehicle=record['vehicle'])
                    new_navigation_record.save()
            return Response({"Message":"Records are created succesfully"}, status=status.HTTP_200_OK)
        except:
            raise Exception("Something weng wrong")
