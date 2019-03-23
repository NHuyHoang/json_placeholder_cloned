from rest_framework import serializers
from api.v1.models.post import Post
from api.v1.serializers.user_serializer import UserSerializer
from api.v1.models.comment import Comment


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    comments = serializers.PrimaryKeyRelatedField(
        queryset=Comment.objects.all(), many=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'author', 'comments')
