from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class User(AbstractUser):
    phone = models.CharField(max_length=10,)
    id = models.CharField(max_length=31, default=uuid.uuid1,
                          primary_key=True, editable=False)
    jwt_secret = models.CharField(
        max_length=31, default=uuid.uuid1, editable=False)

    def __str__(self):
        return self.username

    # def save(self, **kwargs):
    #     if not self.id:
    #         self.id = generate()
    #     super(User, self).save(*kwargs)


    class Meta:
        app_label = "v1"

def jwt_get_secret_key(user_model):
    return user_model.jwt_secret
