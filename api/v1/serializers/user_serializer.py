from rest_framework import serializers
from api.v1.models.user import User
from api.v1.serializers.staff_serializer import StaffSerializer


class UserSerializer(serializers.ModelSerializer):
    companies = StaffSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name',
                  'email', 'phone', 'companies', 'jwt_secret')
