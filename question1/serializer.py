from dataclasses import fields
from rest_framework import serializers
from .models import NavigationRecord, Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    records = serializers.CharField(read_only=True)

    class Meta:
        model = Vehicle
        fields=['id','plate']

class NavigationRecordsSerializer(serializers.ModelSerializer):
    vehicle_plate = serializers.CharField(source='vehicle.plate', read_only=True)
    datetime = serializers.DateTimeField(format="%d.%m.%Y %H:%M:%S")

    class Meta:
        model = NavigationRecord
        fields=['latitude','longitude','datetime','vehicle_plate']