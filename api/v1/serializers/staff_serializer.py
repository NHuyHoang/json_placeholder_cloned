from rest_framework import serializers
from api.v1.models.staff import Staff

class StaffSerializer(serializers.ModelSerializer):

    name = serializers.ReadOnlyField(source='company_staff.name')
    catchPhrase = serializers.ReadOnlyField(source='company_staff.catchPhrase')
    bs = serializers.ReadOnlyField(source='company_staff.bs')

    class Meta:
        model = Staff
        fields = ('name', 'catchPhrase', 'bs')
