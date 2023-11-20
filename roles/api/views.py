from rest_framework.viewsets import ModelViewSet
from roles.models import Role
from roles.api.serializers import RoleSerializer

class RoleApiViewSet(ModelViewSet):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()
