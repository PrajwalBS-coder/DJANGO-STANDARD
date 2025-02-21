from rest_framework.serializers import ModelSerializer,ValidationError
from apps.app2.Models.models import Employee

class Emp_serializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
    def vallidate(self,data):
        if data['name'].lower() == 'admin':
            raise ValidationError("Name can't be admin")
        if data['salary'] < 10000:
            raise ValidationError("Salary can't be less than 10000")
        return data