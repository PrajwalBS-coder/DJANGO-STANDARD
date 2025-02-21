from rest_framework import viewsets,status,response
from apps.app2.serializer.Emp_serializer import Emp_serializer


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