import json
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Bin,Operation,Collection
from datetime import date, datetime



class Question2TestCase(APITestCase):
    
    def test_single_record(self):
        date_time=datetime.now()
      
        bin = Bin.objects.create(latitude="11.11111",longitude="-11.11111")
        operation= Operation.objects.create(name="operation1")
        Collection.objects.create(
            last_collection=date_time,
            collection_frequency=2,
            operation=operation,
            bin=bin)
        response = self.client.get('/q2/collections')
        

        expected=[{
            "collection_frequency": 2,
                "bin": {
                    "id": 1,
                    "latitude": 11.11111,
                    "longitude": -11.11111
                },
                "operation": {
                    "id": 1,
                    "name": "operation1"
                }
            }  
  ]
    
        self.assertEqual(response.data,expected)
        self.assertEqual(response.status_code, status.HTTP_200_OK)