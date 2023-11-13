from django.db import models
from compras.models import Compras
from tiposMateriales.models import TiposMateriales

class ComprasTiposMateriales(models.Model):
    compra = models.ForeignKey(Compras, on_delete=models.CASCADE)
    tipoMaterial = models.ForeignKey(TiposMateriales, on_delete=models.CASCADE)
    precio = models.IntegerField()
    cantidad = models.IntegerField()

    def __str__(self):
        return f"CompraTipoMaterial {self.id}"
