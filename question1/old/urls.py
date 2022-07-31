from django.urls import path
from . import views

app_name="question1"
urlpatterns = [
    path('',views.index,name='index'),
    path('basic-solution/<int:vehicle_id>',views.basicSolution,name='basic_solution'),

    path('api/create-dummy-vehicles/<int:record_num>',views.createDummyVehicles,name='create_dummy_vehicles'),
    path('api/create-dummy-navigation-records/<int:record_num>',views.createDummyNavigationRecords,name='create_dummy_navigation_records'),


]
