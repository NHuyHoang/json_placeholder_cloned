from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from api.v1.serializers.post_serializer import PostSerializer
from api.v1.models.post import Post
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


# @permission_classes([list(self,request,*args,**kwargs):])
class PostView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly, )