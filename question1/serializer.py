from rest_framework import serializers
from .models import NavigationRecord, Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    #records = serializers.CharField(read_only=True)

    class Meta:
        model = Vehicle
        fields=['id','plate']

class NavigationRecordsSerializer(serializers.ModelSerializer):
    vehicle_plate = serializers.CharField(source='vehicle.plate', read_only=True)
    datetime = serializers.DateTimeField(format="%d.%m.%Y %H:%M:%S")
    max_date = serializers.DateTimeField(format="%d.%m.%Y %H:%M:%S")


    class Meta:
        model = NavigationRecord
        fields=['latitude','longitude','datetime','max_date','vehicle_plate']

class LastPointSerializer(serializers.ModelSerializer):
    datetime = serializers.DateTimeField(format="%d.%m.%Y %H:%M:%S")
    vehicle_plate = serializers.CharField(read_only=True)
    latitude = serializers.CharField(read_only=True)
    longitude = serializers.CharField(read_only=True)


    class Meta:
        model = NavigationRecord
        fields=['latitude','longitude','vehicle_plate','datetime']

