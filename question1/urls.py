from django.urls import path
from .views import VehicleListView, VehicleDetailView,VehicleNavigationRecordsView,CreateDummyVehiclesView,CreateDummyNavigationRecordsView

app_name="question1"
urlpatterns = [
    path('get-vehicles',VehicleListView.as_view(),name='vehicles_list'),
    path('get-vehicle/<int:vehicle_id>',VehicleDetailView.as_view(),name='vehicle_detail'),
    path('get-vehicle-navigation-records/<int:vehicle_id>',VehicleNavigationRecordsView.as_view(),name='vehicle_navigation_records'), 
    path('create-dummy-vehicles/<int:record_num>',CreateDummyVehiclesView.as_view(),name='create_dummy_vehicles'),
    path('create-dummy-navigation-records/<int:record_num>',CreateDummyNavigationRecordsView.as_view(),name='create_dummy_navigation_records'),


]
