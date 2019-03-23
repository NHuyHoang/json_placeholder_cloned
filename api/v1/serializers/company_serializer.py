from rest_framework import serializers
from api.v1.models.company import Company
from api.v1.models.user import User
from django.forms.models import model_to_dict


class StaffRelatedField(serializers.RelatedField):

    def to_representation(self, value):
        dict_obj = model_to_dict(value)
        return dict_obj


class CompanySerizlier(serializers.ModelSerializer):
    queryset = User.objects.all()
    staffs = StaffRelatedField(queryset=queryset, many=True,)

    class Meta:
        model = Company
        fields = ('name', 'catchPhrase', 'bs', 'staffs')
