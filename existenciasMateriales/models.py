from django.db import models
from tiposMateriales.models import TiposMateriales

class ExistenciasMateriales(models.Model):
    tipoMaterial = models.ForeignKey(TiposMateriales, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"ExistenciaMaterial {self.id}"
