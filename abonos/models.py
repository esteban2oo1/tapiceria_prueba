from django.db import models
from creditos.models import Creditos

class Abonos(models.Model):
    credito = models.ForeignKey(Creditos, on_delete=models.CASCADE)
    monto = models.IntegerField()
    fecha_abono = models.DateField()

    def __str__(self):
        return f"Abono {self.id}"
