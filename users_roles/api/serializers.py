from rest_framework import serializers
from users_roles.models import UsuariosRoles

class UsuariosRolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuariosRoles
        fields = '__all__'
