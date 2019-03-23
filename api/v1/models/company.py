from django.db import models
from .user import User

class Company(models.Model):
    name = models.CharField(max_length=100)
    catchPhrase = models.CharField(max_length=256)
    bs = models.CharField(max_length=256)
    staffs = models.ManyToManyField(User, through='staff')

    def __str__(self):
        return self.name

    class Meta:
        app_label = "v1"