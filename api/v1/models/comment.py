from django.db import models
from .post import Post
from .user import User
import uuid

class Comment(models.Model):
    id = models.CharField(max_length=21, primary_key=True, default=uuid.uuid4 , editable=False)
    message = models.TextField()
    date_add = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments',)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')


    class Meta:
        app_label = "v1"

    def __str__(self):
        return self.id
