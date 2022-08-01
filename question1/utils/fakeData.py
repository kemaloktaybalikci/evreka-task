from faker import Faker
from faker.providers import automotive,date_time,geo
from ..models import  Vehicle


fake=Faker()
fake.add_provider({automotive,date_time,geo})
class FakeDataGenerator():
    def make_navigation_records(num):
        fake_navigation_records = [{'x':x,
            'datetime':fake.date_time_this_year({"before_now": True, "after_now": False}),
            'latitude':fake.latitude(),'longitude':fake.longitude(),
            'vehicle':Vehicle.objects.random()
             } for x in range(int(num))]
        return fake_navigation_records

    def make_vehicles(num): 
        fake_vehicles = [{'plate':fake.license_plate()} for x in range(int(num))]
        return fake_vehicles

