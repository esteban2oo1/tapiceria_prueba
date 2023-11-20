from rest_framework import viewsets
from users_roles.models import UsuariosRoles
from users_roles.api.serializers import UsuariosRolesSerializer

class UsuariosRolesViewSet(viewsets.ModelViewSet):
    queryset = UsuariosRoles.objects.all()
    serializer_class = UsuariosRolesSerializer
