from rest_framework.routers import DefaultRouter
from users_roles.api.views import UsuariosRolesViewSet

router_usuariosRoles = DefaultRouter()
router_usuariosRoles.register(r'usuariosroles', UsuariosRolesViewSet, basename='usuariosroles')
