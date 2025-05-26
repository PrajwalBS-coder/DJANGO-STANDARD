from django.urls import path
from apps.app3.API.prediction import GetPredictions
from apps.app3.API.upload_images import UploadImageView

urlpatterns = [
    path('prediction/',GetPredictions.as_view(),name='prediction'),
    path('upload-images/',UploadImageView.as_view(),name='upload-image'),
]