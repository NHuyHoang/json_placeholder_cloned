from rest_framework import generics, viewsets, views, status
from rest_framework.permissions import IsAuthenticated
from api.v1.models.user import User
from api.v1.serializers.user_serializer import UserSerializer
from rest_framework.response import Response
import uuid


class UserList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class Logout(views.APIView):
    permission_classes = ([IsAuthenticated])

    def post(self, request, *args, **kwargs):
        user = request.user
        user.jwt_secret = uuid.uuid4()
        user.save()
        print(user.jwt_secret)
        return Response(status=status.HTTP_204_NO_CONTENT)
