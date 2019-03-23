from django.db import models
import uuid
from .user import User

class Post(models.Model):
    id = models.CharField(max_length=21, primary_key=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=256)
    body = models.TextField()
    author = models.ForeignKey(User,related_name='author', on_delete=models.CASCADE)

   
    
    class Meta:
        app_label = "v1"

    def __str__(self):
        return self.title