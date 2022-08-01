import collections
from this import s
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import CollectionSerializer
from .models import  Collection
import json


# Create your views here.
class CollectionListView(APIView):
    def get(self, request):
        collections = Collection.objects.filter().all()
        serializer = CollectionSerializer(collections, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CollectionFrequencyListView(APIView):
    def get(self, request):
        collections = Collection.objects.filter().all()
        list=[]
        for item in collections:
            list.append(((item.bin.id,item.operation.name),item.collection_frequency))

        return Response(json.dumps(list), status=status.HTTP_200_OK)
