from rest_framework.serializers import ModelSerializer
from apps.app2.Models.models import Employee

class Emp_serializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'