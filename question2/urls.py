from django.urls import path
from .views import CollectionListView

app_name="question2"
urlpatterns = [   
    path('collections',CollectionListView.as_view(),name='collection_list'),

]
