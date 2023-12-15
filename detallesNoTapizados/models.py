from django.db import models
from colores.models import Colores
from productos.models import Productos
from tiposMateriales.models import TiposMateriales

class DetallesNoTapizados(models.Model):
    color = models.ForeignKey(Colores, on_delete=models.CASCADE)
    tipoMaterial = models.ForeignKey(TiposMateriales, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad_tipoMaterial = models.IntegerField(default=0)
    cantidad_producto = models.IntegerField(default=0)
    
    def _str_(self):
        return f"{self.color.nombre} - {self.tipoMaterial.nombre} - {self.producto.descripcion} - {self.cantidad_tipoMaterial} - {self.cantidad_producto}"