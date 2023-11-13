from django.db import models
from django.contrib.auth.models import User

class Compras(models.Model):
    comprador = models.ForeignKey('users.User', related_name='comprador_compras', on_delete=models.CASCADE)
    proveedor = models.ForeignKey('users.User', related_name='proveedor_compras', on_delete=models.CASCADE)
    fecha_compra = models.DateField(null=True)

    def __str__(self):
        return f"Compra {self.id}"
