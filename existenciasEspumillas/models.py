from django.db import models
from tiposEspumillas.models import TiposEspumillas

class ExistenciasEspumillas(models.Model):
    tipoEspumilla = models.ForeignKey(TiposEspumillas, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"ExistenciaEspumilla {self.id}"
