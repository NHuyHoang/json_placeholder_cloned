from rest_framework import generics
from api.v1.models.company import Company
from api.v1.serializers.company_serializer import CompanySerizlier

class CompanyList(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerizlier

    