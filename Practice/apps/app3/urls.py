from django.urls import path
from apps.app3.API.prediction import Get_Predictions

urlpatterns = [
    path('prediction/',Get_Predictions.as_view(),name='prediction')
]