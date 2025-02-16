from django.urls import path
from app1.API.UserAdd import CreateUser
from app1.API.UserLogin import Login


urlpatterns=[
    path('add-user/',CreateUser.as_view(),name='user'),
    path('user-login/',Login.as_view(),name='user-login')
]