from rest_framework import serializers
from api.v1.models.comment import Comment
from api.v1.serializers.user_serializer import UserSerializer

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Comment
        fields = ('id', 'message', 'date_add', 'user',)
