
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import rest_framework.response as response
from rest_framework import status


@swagger_auto_schema(
    responses={
        201 : openapi.Response(description='Created User SuccessFully'),
        400 : "Bad Request"
    },
    operation_description="Checking For Access",
    operation_summary="APi For Checking For Access",
    operation_id="Checking For Access API"
)
class CheckAccess(APIView):
   def get(self,request):
      try:
         return response.Response({"Message":"You Have Access"} ,status=status.HTTP_200_OK)
      except Exception as e:
         return response.Response(status=status.HTTP_401_UNAUTHORIZED)