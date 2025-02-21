from rest_framework import status, views, response
from rest_framework import viewsets
from apps.app2.serializer.Emp_serializer import Emp_serializer

class Add_user(viewsets.generics.CreateAPIView):  
    serializer_class = Emp_serializer
    queryset = Emp_serializer.Meta.model.objects.all()

    def post(self, request, *args, **kwargs):
        context ={}
        state=status.HTTP_201_CREATED
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                context["data"]=serializer.data
                context["message"]="User added successfully"
            else:
                context['error'] = 'Invalid data'
                state=status.HTTP_400_BAD_REQUEST
        except Exception as e:
            context["message"]= str(e)
            state=status.HTTP_400_BAD_REQUEST
        return response.Response(context, state)
