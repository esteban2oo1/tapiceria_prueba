from django.db import models
from colores.models import Colores
from productos.models import Productos

class DetallesNoTapizados(models.Model):
    color = models.ForeignKey(Colores, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.color} - {self.producto}"