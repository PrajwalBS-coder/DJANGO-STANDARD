from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ImageSerializer
from rest_framework.parsers import MultiPartParser, FormParser

class UploadImageView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            image_instance = serializer.save()
            return Response({
                'message': 'Image uploaded successfully',
                'image_id': image_instance.id
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)