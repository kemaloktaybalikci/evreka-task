from django.urls import path
from .views import VehicleListView, VehicleDetailView,VehicleNavigationRecordsView,CreateDummyVehiclesView,CreateDummyNavigationRecordsView

app_name="question1"
urlpatterns = [
    path('vehicles/last-points>',VehicleNavigationRecordsView.as_view(),name='vehicle_last_points'), 

    path('vehicles',VehicleListView.as_view(),name='vehicles_list'),
    path('vehicles/<int:vehicle_id>',VehicleDetailView.as_view(),name='vehicle_detail'),
    path('vehicles/dummy-data/<int:record_num>',CreateDummyVehiclesView.as_view(),name='create_dummy_vehicles'),
    path('navigation-records/dummy-data/<int:record_num>',CreateDummyNavigationRecordsView.as_view(),name='create_dummy_navigation_records'),

]
