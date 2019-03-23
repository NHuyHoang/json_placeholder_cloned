from django.db import models
from .user import User
from .company import Company

class Staff(models.Model):
    companies = models.ForeignKey(User, related_name='companies', on_delete=models.CASCADE)
    company_staff = models.ForeignKey(Company, related_name='company_staff', on_delete=models.CASCADE)
    date_add = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = "v1"
        unique_together = (("companies", "company_staff"),)
    
    

    