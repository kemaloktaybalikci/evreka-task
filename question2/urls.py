from django.urls import path
from .views import CollectionListView,CollectionFrequencyListView

app_name="question2"
urlpatterns = [
    path('get-collections',CollectionListView.as_view(),name='collection_list'),
    path('get-collection-frequency-list',CollectionFrequencyListView.as_view(),name='collection_frequency_list'),

]
