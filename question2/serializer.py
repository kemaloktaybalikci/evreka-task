from rest_framework import serializers
from .models import Bin, Operation,Collection


class BinSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bin
        fields=['id','latitude','longitude']

class OperationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Operation
        fields=['id','name']


class CollectionSerializer(serializers.ModelSerializer):
    collection_frequency = serializers.IntegerField(read_only=True)
    #last_collection = serializers.DateTimeField(format="%d.%m.%Y %H:%M:%S")
    bin = BinSerializer()
    operation = OperationSerializer()

    
    class Meta:
        model = Collection
        fields=['collection_frequency','bin','operation']

