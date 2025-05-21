# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from drf_yasg.utils import swagger_auto_schema
# from drf_yasg import openapi
# import os
# import uuid
# from datetime import datetime
# from rest_framework.parsers import MultiPartParser, FormParser

# class Upload_Image(APIView):
#     parser_classes = [MultiPartParser, FormParser]
#     permission_classes = [IsAuthenticated]
#     MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB limit

#     @swagger_auto_schema(
#         manual_parameters=[
#             openapi.Parameter(
#                 name='image',
#                 in_=openapi.IN_FORM,
#                 type=openapi.TYPE_FILE,
#                 description='Image file to upload (JPG, PNG, JPEG)',
#                 required=True
#             )
#         ],
#         responses={
#             200: openapi.Response(description='Image uploaded successfully'),
#             400: "Bad Request - Invalid file type or no file provided",
#             500: "Internal Server Error"
#         },
#         operation_description="User Image Upload API",
#         operation_summary="API for user Image Upload",
#         operation_id="USER-IMAGE-UPLOAD-API"
#     )
#     def post(self, request):
#         # your existing logic
#         try:
#             image = request.FILES.get('image')
            
#             if not image:
#                 return Response(
#                     {'error': 'No image file provided'},
#                     status=status.HTTP_400_BAD_REQUEST
#                 )

#             # File size validation
#             if image.size > self.MAX_FILE_SIZE:
#                 return Response(
#                     {'error': f'File size too large. Maximum size is {self.MAX_FILE_SIZE/1024/1024}MB'},
#                     status=status.HTTP_400_BAD_REQUEST
#                 )

#             # Validate file type
#             allowed_types = ['image/jpeg', 'image/png', 'image/jpg']
#             if image.content_type not in allowed_types:
#                 return Response(
#                     {'error': 'Invalid file type. Only JPG, JPEG, and PNG are allowed'},
#                     status=status.HTTP_400_BAD_REQUEST
#                 )

#             # Create unique filename
#             file_extension = os.path.splitext(image.name)[1]
#             unique_filename = f"{uuid.uuid4()}{file_extension}"
            
#             # Create uploads directory with date-based structure
#             current_date = datetime.now()
#             upload_dir = os.path.join('media', 'uploads', 
#                                     str(current_date.year),
#                                     str(current_date.month))
#             os.makedirs(upload_dir, exist_ok=True)

#             # Save the file
#             file_path = os.path.join(upload_dir, unique_filename)
#             print("file_path",file_path)
            
#             # Secure file handling
#             try:
#                 with open(file_path, 'wb+') as destination:
#                     for chunk in image.chunks():
#                         destination.write(chunk)
#             except IOError as e:
#                 return Response(
#                     {'error': 'Failed to save file'},
#                     status=status.HTTP_500_INTERNAL_SERVER_ERROR
#                 )

#             return Response(
#                 {
#                     'message': 'Image uploaded successfully',
#                     'file_name': unique_filename,
#                     'file_path': file_path
#                 },
#                 status=status.HTTP_200_OK
#             )

#         except Exception as e:
#             return Response(
#                 {'error': f'An unexpected error occurred: {str(e)}'},
#                 status=status.HTTP_500_INTERNAL_SERVER_ERROR
#             )
        
# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from drf_yasg.utils import swagger_auto_schema
# from drf_yasg import openapi
# from rest_framework.parsers import MultiPartParser, FormParser

# import os
# import uuid
# from datetime import datetime
# from PIL import Image
# from io import BytesIO
# import traceback


# class Upload_Image(APIView):
#     parser_classes = [MultiPartParser, FormParser]
#     permission_classes = [IsAuthenticated]
#     MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

#     @swagger_auto_schema(
#         manual_parameters=[
#             openapi.Parameter(
#                 name='image',
#                 in_=openapi.IN_FORM,
#                 type=openapi.TYPE_FILE,
#                 description='Image file to upload (JPG, PNG, JPEG)',
#                 required=True
#             )
#         ],
#         responses={
#             200: openapi.Response(description='Image uploaded successfully'),
#             400: "Bad Request - Invalid file type or no file provided",
#             500: "Internal Server Error"
#         },
#         operation_description="User Image Upload API",
#         operation_summary="API for user Image Upload",
#         operation_id="USER-IMAGE-UPLOAD-API"
#     )
#     def post(self, request):
#         try:
#             image = request.FILES.get('image')

#             if not image:
#                 return Response({'error': 'No image file provided'}, status=status.HTTP_400_BAD_REQUEST)

#             # File size check
#             if image.size > self.MAX_FILE_SIZE:
#                 return Response(
#                     {'error': f'File size too large. Max allowed is {self.MAX_FILE_SIZE // (1024 * 1024)} MB'},
#                     status=status.HTTP_400_BAD_REQUEST
#                 )

#             # Check MIME type
#             allowed_types = ['image/jpeg', 'image/png', 'image/jpg']
#             if image.content_type not in allowed_types:
#                 return Response(
#                     {'error': 'Invalid file type. Only JPG, JPEG, and PNG are allowed'},
#                     status=status.HTTP_400_BAD_REQUEST
#                 )

#             # Validate actual image content using Pillow
#             try:
#                 img = Image.open(BytesIO(image.read()))
#                 img.verify()
#                 image.seek(0)  # Reset stream after reading
#             except Exception:
#                 return Response(
#                     {'error': 'Uploaded file is not a valid image'},
#                     status=status.HTTP_400_BAD_REQUEST
#                 )

#             # Generate unique filename
#             file_extension = os.path.splitext(image.name)[1]
#             unique_filename = f"{uuid.uuid4()}{file_extension}"

#             # Create upload directory
#             now = datetime.now()
#             upload_dir = os.path.join('media', 'uploads', str(now.year), str(now.month))
#             os.makedirs(upload_dir, exist_ok=True)

#             file_path = os.path.join(upload_dir, unique_filename)

#             # Save file securely
#             with open(file_path, 'wb+') as destination:
#                 for chunk in image.chunks():
#                     destination.write(chunk)

#             return Response({
#                 'message': 'Image uploaded successfully',
#                 'file_name': unique_filename,
#                 'file_path': file_path
#             }, status=status.HTTP_200_OK)

#         except Exception as e:
#             traceback.print_exc()  # Debugging help in logs
#             return Response(
#                 {'error': f'An unexpected error occurred: {str(e)}'},
#                 status=status.HTTP_500_INTERNAL_SERVER_ERROR
#             )

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import os, uuid
from datetime import datetime
from PIL import Image
from io import BytesIO
import traceback


class Upload_Image(APIView):
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
        try:
            image = request.FILES.get('image')
            if not image:
                return Response({'error': 'No file provided'}, status=400)

            # Size check
            if image.size > self.MAX_FILE_SIZE:
                return Response({'error': 'File size too large'}, status=400)

            # Type check
            if image.content_type not in ['image/jpeg', 'image/png', 'image/jpg']:
                return Response({'error': 'Invalid file type'}, status=400)

            # Validate actual image
            try:
                img = Image.open(image)
                img.verify()
                image.seek(0)
            except Exception:
                return Response({'error': 'Invalid image file'}, status=400)

            # File saving
            file_ext = os.path.splitext(image.name)[1]
            filename = f"{uuid.uuid4()}{file_ext}"
            today = datetime.now()
            upload_dir = os.path.join('media', 'uploads', str(today.year), str(today.month))
            os.makedirs(upload_dir, exist_ok=True)
            path = os.path.join(upload_dir, filename)

            with open(path, 'wb+') as dest:
                for chunk in image.chunks():
                    dest.write(chunk)

            return Response({'message': 'Uploaded', 'file_path': path}, status=200)

        except Exception as e:
            traceback.print_exc()
            return Response({'error': str(e)}, status=500)
