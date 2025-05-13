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
                'refresh': openapi.Schema(type=openapi.TYPE_STRING, description='Refresh token')
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
        context = {}
        status_code = status.HTTP_200_OK
        try:
            refresh_token = request.data.get('refresh')
            auth_header = request.META.get('HTTP_AUTHORIZATION', '')

            if not refresh_token:
                context['error'] = "Refresh token is required"
                return response.Response(context, status=status.HTTP_400_BAD_REQUEST)

            if not auth_header.startswith('Bearer '):
                context['error'] = "Authorization header with Bearer token is required"
                return response.Response(context, status=status.HTTP_400_BAD_REQUEST)

            # Optional: blacklist refresh token only
            RefreshToken(refresh_token).blacklist()

            context['message'] = "Logged out successfully"
        except Exception as e:
            context['error'] = str(e)
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response.Response(context, status=status_code)
