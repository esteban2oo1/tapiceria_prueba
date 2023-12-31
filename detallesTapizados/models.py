from django.db import models
from tiposTelas.models import TiposTelas
from colores.models import Colores
from productos.models import Productos
from tiposEspumillas.models import TiposEspumillas
from tiposMateriales.models import TiposMateriales

class DetallesTapizados(models.Model):
    tipoTela = models.ForeignKey(TiposTelas, on_delete=models.CASCADE)
    color = models.ForeignKey(Colores, on_delete=models.CASCADE)
    tipoEspumilla = models.ForeignKey(TiposEspumillas, on_delete=models.CASCADE)
    tipoMaterial = models.ForeignKey(TiposMateriales, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad_telaColor = models.IntegerField(default=0)
    cantidad_tipoEspumilla = models.IntegerField(default=0)
    cantidad_tipoMaterial = models.IntegerField(default=0)
    cantidad_producto = models.IntegerField(default=0)

    def str(self):
        return f"{self.tipoTela.nombre} - {self.color.nombre} - {self.tipoEspumilla.nombre} - {self.tipoMaterial.nombre} - {self.producto.descripcion} - {self.cantidad_telaColor} - {self.cantidad_tipoEspumilla} - {self.cantidad_tipoMaterial} - {self.cantidad_producto}"