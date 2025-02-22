from rest_framework import viewsets,status,response
from rest_framework.views import APIView
from apps.app2.serializer.Emp_serializer import Emp_serializer
from apps.app2.Models.models import Employee
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class ListOutEmp(viewsets.generics.RetrieveAPIView):
    serializer_class = Emp_serializer
    queryset = Emp_serializer.Meta.model.objects.all()

    def get(self, request, *args, **kwargs):
        context = {}
        state = status.HTTP_200_OK
        try:
            queryset = self.get_queryset()
            if queryset:
                serializer = self.get_serializer(queryset, many=True)
                context['data'] = serializer.data
                context['message'] = 'User data fetched successfully'
            else:
                context['message'] = 'No data found'
        except Exception as e:
            context['message'] = str(e)
            state = status.HTTP_400_BAD_REQUEST
        return response.Response(context, state)
    
class Joson(APIView):
    @swagger_auto_schema(
    responses={
        201 : openapi.Response(description='Created User SuccessFully'),
        400 : "Bad Request"
    },
    operation_description="Checking For Access",
    operation_summary="APi For Checking For Access",
    operation_id="Checking For Access API"
)
    def get(self,request,id):
        id=int(id)
        print(id,type(id))
        # data=Employee.objects.filter(meta_data__icontains='"id": {id}"')
        data = Employee.objects.filter(meta_data__icontains=f'"id": {id}')
        serializer=Emp_serializer(data,many=True)
        return response.Response(serializer.data)





    

# class Joson(APIView):
#     @swagger_auto_schema(
#         responses={
#             201: openapi.Response(description='Created User Successfully'),
#             400: "Bad Request"
#         },
#         operation_description="Checking For Access",
#         operation_summary="API For Checking Access",
#         operation_id="Checking For Access API"
#     )
#     def get(self, request, id):  # ✅ Add `self, request` as first parameters
#         id = int(id)
#         print(id, type(id))

#         # ✅ Correct the filter query (using f-string)
#         data = Employee.objects.filter(meta_data__icontains=f'"id": {id}')

#         # ✅ Serialize the queryset
#         serializer = Emp_serializer(data, many=True)

#         return response.Response(serializer.data)  # ✅ Use `Response` properly