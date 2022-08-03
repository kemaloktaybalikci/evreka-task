import json
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from .models import Vehicle,NavigationRecord
from datetime import  datetime, timedelta



class Question1TestCase(APITestCase):
    
    def test_single_record(self):
        url = reverse('question1:vehicle_last_points')
        date_time=datetime.now()
        
        test_vehicle = Vehicle.objects.create(plate="AAA-123")
        test_navigation_record = NavigationRecord.objects.create(
            datetime=date_time,
            latitude=11.11111,
            longitude=-11.11111,
            vehicle=test_vehicle)
        response = self.client.get('/q1/vehicles/last-points')
        

        expected={
            "last_points":[
                {
                "latitude": "11.11111",
                "longitude": "-11.11111",
                "vehicle_plate": "AAA-123",
                "datetime": date_time.strftime("%d.%m.%Y %H:%M:%S")
                }
            ]
        }
    
        self.assertEqual(response.data,expected)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_multiple_record(self):
        url = reverse('question1:vehicle_last_points')
        date_time=datetime.now()
        plates=["AAA-111","BBB-222"]
        latitudes=[11.11111,22.22222,33.33333,44.44444]
        longitudes=[-11.11111,-22.22222,-33.33333,-44.44444]

        test_vehicles=[]
        test_vehicles.append(Vehicle.objects.create(plate=plates[0]))
        test_vehicles.append(Vehicle.objects.create(plate=plates[1]))

        NavigationRecord.objects.create(datetime=date_time-timedelta(hours=0),vehicle=test_vehicles[0],latitude=latitudes[0],longitude=longitudes[0])      #proper
        NavigationRecord.objects.create(datetime=date_time-timedelta(hours=20),vehicle=test_vehicles[1],latitude=latitudes[1],longitude=longitudes[1])     #proper
        NavigationRecord.objects.create(datetime=date_time-timedelta(hours=60),vehicle=test_vehicles[0],latitude=latitudes[2],longitude=longitudes[2])     #improper
        NavigationRecord.objects.create(datetime=date_time+timedelta(hours=20),vehicle=test_vehicles[1],latitude=latitudes[3],longitude=longitudes[3])     #improper
        
        response = self.client.get('/q1/vehicles/last-points')
        expected={
            "last_points":[
                {
                "latitude": "11.11111",
                "longitude": "-11.11111",
                "vehicle_plate": "AAA-111",
                "datetime": (date_time-timedelta(hours=0)).strftime("%d.%m.%Y %H:%M:%S")
                
                },
                {
                "latitude": "22.22222",
                "longitude": "-22.22222",
                "vehicle_plate": "BBB-222",
                "datetime": (date_time-timedelta(hours=20)).strftime("%d.%m.%Y %H:%M:%S")
                }
            ]
        }
        
        self.assertEqual(json.dumps(response.data),json.dumps(expected))
        self.assertEqual(response.status_code, status.HTTP_200_OK)