from rest_framework.generics import GenericAPIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import status,response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.authentication import authenticate
from rest_framework.exceptions import ValidationError

class Get_Predictions(GenericAPIView):
    @swagger_auto_schema(
    operation_id= 'Prediction',
    operation_description= "Prediction",
    tags= ["Prediction"],
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'type':openapi.Schema(
                type=openapi.TYPE_ARRAY,
                description='your type for prediction',
                items=openapi.Items(type=openapi.TYPE_STRING)

            ),
        },
        
    ),
    responses={
        status.HTTP_200_OK : openapi.Response("Loged in Successfully"),
        status.HTTP_400_BAD_REQUEST : openapi.Response('Bad Request'),
        status.HTTP_500_INTERNAL_SERVER_ERROR : openapi.Response("Server error")
    }
    )
    def get(self,request):
        pass