from django.db import models
from compras.models import Compras
from tiposEspumillas.models import TiposEspumillas

class ComprasTiposEspumillas(models.Model):
    compra = models.ForeignKey(Compras, on_delete=models.CASCADE)
    tipoEspumilla = models.ForeignKey(TiposEspumillas, on_delete=models.CASCADE)
    precio = models.IntegerField()
    cantidad = models.IntegerField()

    def __str__(self):
        return f"CompraTipoEspumilla {self.id}"
