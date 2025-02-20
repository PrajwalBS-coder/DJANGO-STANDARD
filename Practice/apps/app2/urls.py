from django.urls import path
from apps.app2.api.add_user import Add_user

urlpatterns = [
    path('add_user/', Add_user.as_view(), name='add_user'),
]