from django.db import models
from productos.models import Productos

class ExistenciasProductos(models.Model):
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"ExistenciaProducto {self.id}"
