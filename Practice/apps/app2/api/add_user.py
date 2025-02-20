from rest_framework import status, views, response
from rest_framework import viewsets
from apps.app2.serializer.Emp_serializer import Emp_serializer

class Add_user(viewsets.generics.CreateAPIView):  
    serializer_class = Emp_serializer
    queryset = Emp_serializer.Meta.model.objects.all()

    def post(self, request, *args, **kwargs):
        context ={}
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                context["data"]=serializer.data
                context["message"]="User added successfully"
            context['error'] = 'Invalid data'
        except Exception as e:
            return response.Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return response.Response(context, status=status.HTTP_201_CREATED)
