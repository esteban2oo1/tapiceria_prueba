from django.db import models
from colores.models import Colores
from productos.models import Productos

class DetallesNoTapizados(models.Model):
    color = models.ForeignKey(Colores, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad_tipoMaterial = models.IntegerField(default=0)
    cantidad_producto = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.color.nombre} - {self.producto.descripcion} - {self.cantidad_tipoMaterial} - {self.cantidad_producto}"