from django.contrib import admin
from .models import Collection, Bin, Operation
    
class BinAdmin(admin.ModelAdmin):
    list_display= ["id","longitude","latitude"]

class OperationAdmin(admin.ModelAdmin):
    list_display= ["id","name"]

class CollectionAdmin(admin.ModelAdmin):
    list_display= ["id","bin","operation"]

admin.site.register(Collection,CollectionAdmin)
admin.site.register(Bin,BinAdmin)
admin.site.register(Operation,OperationAdmin)