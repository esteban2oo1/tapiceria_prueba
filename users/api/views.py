from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User
from users.api.serializers import UserSerializer, GroupSerializer
from django.contrib.auth.models import Group
from rest_framework_simplejwt.tokens import RefreshToken

class UserApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        request.data['password'] = make_password(request.data['password'])
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(email=request.data['email'])
        refresh = RefreshToken.for_user(user)
        tokens = {'refresh': str(refresh), 'access': str(refresh.access_token)}
        response.data['tokens'] = tokens
        return response

    def partial_update(self, request, *args, **kwargs):
        password = request.data.get('password', None)
        if password:
            request.data['password'] = make_password(password)
        else:
            request.data.pop('password', None)
        return super().partial_update(request, *args, **kwargs)

class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

class GroupApiViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = GroupSerializer
    queryset = Group.objects.all()