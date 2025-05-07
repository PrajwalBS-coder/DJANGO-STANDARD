from django.urls import path
from apps.app3.API.prediction import GetPredictions

urlpatterns = [
    path('prediction/',GetPredictions.as_view(),name='prediction'),
]