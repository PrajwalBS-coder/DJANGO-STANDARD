from rest_framework.generics import GenericAPIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import status, response
from rest_framework.permissions import AllowAny

class GetPredictions(GenericAPIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_id='Prediction',
        operation_description="Prediction API endpoint",
        tags=["Prediction"],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'type': openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    description='Your type for prediction',
                    items=openapi.Items(type=openapi.TYPE_STRING)
                ),
            },
            required=['type']
        ),
        responses={
            status.HTTP_200_OK: openapi.Response("Logged in Successfully"),
            status.HTTP_400_BAD_REQUEST: openapi.Response('Bad Request'),
            status.HTTP_500_INTERNAL_SERVER_ERROR: openapi.Response("Server error")
        }
    )
    def post(self, request):
        try:
            prediction_type = request.data.get('type')
            if not prediction_type:
                return response.Response(
                    {"error": "Type is required"}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Add your prediction logic here
            result = {"prediction": "Your prediction result"}
            
            return response.Response(result, status=status.HTTP_200_OK)
            
        except Exception as e:
            return response.Response(
                {"error": str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )