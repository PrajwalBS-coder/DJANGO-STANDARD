from rest_framework import serializers
from django.contrib.auth.models import User



class User_Serializer(serializers.ModelSerializer):
    Is_Super_admin=serializers.BooleanField(default=False,write_only=True)


    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password','Is_Super_admin']
        # fields='__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        choice=validated_data.pop('Is_Super_admin')
        if not choice:
            user = User.objects.create_user(**validated_data,is_staff=True)
        else:
            user=User.objects.create_superuser(**validated_data)
        return user