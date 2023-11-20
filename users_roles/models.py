from django.db import models
from roles.models import Role

class UsuariosRoles(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    rol = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.rol.nombre}"
