from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from app1.Serializers.UserSerializer import User_Serializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from django.conf import settings
from django.core.mail import send_mail


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
    serializer_class = User_Serializer

    def perform_create(self, serializer):
        user = serializer.save()
        
        subject = 'Welcome to Our Platform'
        message = f'Hi {user.username},\n\nThank you for registering with us. Your account has been successfully created.\n\nBest regards,\nThe Team'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [user.email]
        
        try:
            send_mail(
                subject,
                message,
                from_email,
                recipient_list,
                # fail_silently=False,
            )
        except Exception as e:
            import logging
            logger = logging.getLogger('api_logger')
            logger.error(f'Failed to send registration email to {user.email}: {str(e)}')