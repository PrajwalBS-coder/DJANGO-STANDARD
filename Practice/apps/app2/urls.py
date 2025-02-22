from django.urls import path
from apps.app2.api.add_user import Add_user
from apps.app2.api.list_out_users import ListOutEmp, Joson

urlpatterns = [
    path('add_user/', Add_user.as_view(), name='add_user'),
    path('list_out_users/', ListOutEmp.as_view(), name='list_out_users'),
    path('json/<int:id>/', Joson.as_view(), name='json'),

]