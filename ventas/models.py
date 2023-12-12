from django.db import models
from django.contrib.auth.models import User

class Ventas(models.Model):
    comprador = models.ForeignKey('users.User', related_name='comprador_ventas', on_delete=models.CASCADE)
    vendedor = models.ForeignKey('users.User', related_name='vendedor_ventas', on_delete=models.CASCADE)
    fecha_venta = models.DateField(null=True)

    def __str__(self):
        return f"Venta {self.id}"