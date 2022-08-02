import collections
from this import s
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from yaml import serialize
from .serializer import CollectionSerializer
from .models import  Collection
import json


# Create your views here.
class CollectionListView(APIView):
    def get(self, request):
        try:
            collections = Collection.objects.all()
            serializer = CollectionSerializer(collections, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            raise Exception("Something went wrong")