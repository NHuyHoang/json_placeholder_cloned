from rest_framework import generics, viewsets
from rest_framework.response import Response
from api.v1.models.comment import Comment
from django.core import serializers
from api.v1.serializers.comment_serializer import CommentSerializer
from api.v1.models.post import Post
from api.v1.models.user import User
from nanoid import generate
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly

@permission_classes([IsAuthenticatedOrReadOnly])
class CommentDetail(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            id = kwargs['pk']
            cids = Post.objects.get(id=id)
            comments = cids.comments.all()

            def toJson(comment):
                serialized = CommentSerializer(comment)
                return serialized.data

            results = list(map(toJson, comments))
            return Response(results)
        return Response([])


class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        '''
        @param {string} message
        @param {string} user_id
        @param {string} post_id
        '''
        data = request.data
        try:
            user = User.objects.get(id=data['user_id'])
        except User.DoesNotExist:
             return Response(data={"success": False, "message": "User not found"}, status=406)
        try:
            post = Post.objects.get(id=data['post_id'])
        except Post.DoesNotExist:
            return Response(data={"success": False, "message": "Post not found"}, status=406) 

        comment = Comment(
            id=generate(),
            user=user,
            message=data['message'],
            post=post
        )
        comment.save()
        serialized = CommentSerializer(comment)
        return Response(data=serialized.data, status=201)
