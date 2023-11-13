from django.db import models
from compras.models import Compras
from telas_colores.models import TelasColores

class ComprasTelasColores(models.Model):
    compra = models.ForeignKey(Compras, on_delete=models.CASCADE)
    tela_color = models.ForeignKey(TelasColores, on_delete=models.CASCADE)
    precio = models.IntegerField()
    cantidad = models.IntegerField()

    def __str__(self):
        return f"Compra-TelaColor {self.id}"
