from django.urls import path
from .views import UploadImageView
from tests.test_upload import ImageUploadTests

urlpatterns = [
    path('upload/', UploadImageView.as_view(), name='upload-image'),
]