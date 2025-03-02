from django.urls import path
from app1.API.UserAdd import CreateUser
from app1.API.UserLogin import Login
from app1.API.Access import CheckAccess
from .views import trigger_task


urlpatterns=[
    path('add-user/',CreateUser.as_view(),name='user'),
    path('user-login/',Login.as_view(),name='user-login'),
    path('check-access/',CheckAccess.as_view(),name='check-access'),
    path('task/',trigger_task,name='trigger_task')
]