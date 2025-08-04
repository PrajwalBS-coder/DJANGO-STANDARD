from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.app3.serializers import ImageSerializer
from apps.app3.models import Images
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated

class UploadImageView(APIView):

    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticated]
    MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='image',
                in_=openapi.IN_FORM,
                type=openapi.TYPE_FILE,
                description='Image file (JPG, PNG, JPEG)',
                required=True
            )
        ],
        responses={
            200: openapi.Response(description='Image uploaded successfully'),
            400: "Bad Request",
            500: "Internal Server Error"
        }
    )
    def post(self, request):
        data = request.data.copy()
        data['file'] = request.FILES.get('image')
        serializer = ImageSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            image_instance = serializer.save()
            return Response({
                'message': 'Image uploaded successfully',
                'image_id': image_instance.id
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)