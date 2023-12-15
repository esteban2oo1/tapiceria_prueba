from django.db import models
from telas_colores.models import TelasColores
from productos.models import Productos
from tiposEspumillas.models import TiposEspumillas
from tiposMateriales.models import TiposMateriales

class DetallesTapizados(models.Model):
    telaColor = models.ForeignKey(TelasColores, on_delete=models.CASCADE)
    tipoEspumilla = models.ForeignKey(TiposEspumillas, on_delete=models.CASCADE)
    tipoMaterial = models.ForeignKey(TiposMateriales, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad_telaColor = models.IntegerField(default=0)
    cantidad_tipoEspumilla = models.IntegerField(default=0)
    cantidad_tipoMaterial = models.IntegerField(default=0)
    cantidad_producto = models.IntegerField(default=0)

    def _str_(self):
        return f"{self.telaColor.tela.nombre} - {self.tipoEspumilla.nombre} - {self.tipoMaterial.nombre} - {self.producto.descripcion} - {self.cantidad_telaColor} - {self.cantidad_tipoEspumilla} - {self.cantidad_tipoMaterial} - {self.cantidad_producto}"