from django.contrib import admin

# Register your models here.
from .models import NavigationRecord, Vehicle
    
class NavigationRecordAdmin(admin.ModelAdmin):
    list_display= ["id","longitude","latitude","vehicle","datetime"]
class VehicleAdmin(admin.ModelAdmin):
    list_display= ["id","plate"]

admin.site.register(NavigationRecord,NavigationRecordAdmin)
admin.site.register(Vehicle,VehicleAdmin)