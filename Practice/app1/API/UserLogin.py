from rest_framework.generics import GenericAPIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import status,response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from app1.Serializers import LoginSerializer
from rest_framework.permissions import AllowAny

@swagger_auto_schema(
    operation_id= 'User Login',
    operation_description= " Login User",
    tags= ["Login"],
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'username':openapi.Schema(
                type=openapi.TYPE_STRING,
                description='your username'  
            ),
            'password': openapi.Schema(
                type=openapi.TYPE_STRING,
                description='your password' 
            )
        },
        required =['username','password'] ,
    ),
    responses={
        status.HTTP_200_OK : openapi.Response("Loged in Successfully"),
        status.HTTP_400_BAD_REQUEST : openapi.Response('Bad Request'),
        status.HTTP_500_INTERNAL_SERVER_ERROR : openapi.Response("Server error")
    }
)
class Login(GenericAPIView):
    authentication_classes = []  # ✅ Allow login without authentication
    permission_classes = []  # ✅ Allow anyone to access
    serializer_class = LoginSerializer.LoginSerializer
    def post(self,request):
        context = {}
        username=request.data.get('username')
        password = request.data.get('password')

        user=User.objects.filter(username=username).first()


        #refresh token
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        context['access_token']=access_token
        context['refrtesh_token']=str(refresh)

        return response.Response(context)



