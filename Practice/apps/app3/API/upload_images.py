from rest_framework import status, response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class LogOut(APIView):
    """
    API for user logout using JWT tokens
    """
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'refresh': openapi.Schema(type=openapi.TYPE_FILE,
                 description='Refresh token')
            },
            required=['refresh']
        ),
        responses={
            200: openapi.Response(description='Logged out successfully'),
            400: "Bad Request",
            500: "Internal Server Error"
        },
        operation_description="User Logout API",
        operation_summary="API for user logout",
        operation_id="USER-LOGOUT-API"
    )
    def post(self, request):
        pass