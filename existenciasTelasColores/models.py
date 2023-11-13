from django.db import models
from telas_colores.models import TelasColores

class ExistenciasTelasColores(models.Model):
    tela_Color = models.ForeignKey(TelasColores, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"ExistenciaTelaColor {self.id}"
