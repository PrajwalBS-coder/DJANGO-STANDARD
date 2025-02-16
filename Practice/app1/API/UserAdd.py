from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from app1.Serializers.UserSerializer import User_Serializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes


@swagger_auto_schema(
    request_body=User_Serializer,
    responses={
        201 : openapi.Response(description='Created User SuccessFully'),
        400 : "Bad Request"
    },
    operation_description="Create Users",
    operation_summary="APi For User Creation",
    operation_id="CREATE-APi"
)
@permission_classes([IsAuthenticated])
class CreateUser(CreateAPIView):
    serializer_class=User_Serializer