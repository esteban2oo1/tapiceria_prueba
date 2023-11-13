from django.db import models
from tiposTelas.models import TiposTelas
from colores.models import Colores

class TelasColores(models.Model):
    tela = models.ForeignKey(TiposTelas, on_delete=models.CASCADE)
    color = models.ForeignKey(Colores, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.tela.nombre} - {self.color.nombre}'
