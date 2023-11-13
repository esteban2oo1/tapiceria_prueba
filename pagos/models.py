from django.db import models
from ventasProductos.models import VentasProductos

class Pagos(models.Model):
    monto = models.IntegerField()
    fecha_pago = models.DateField()
    ventaProducto = models.ForeignKey(VentasProductos, on_delete=models.CASCADE)

    def __str__(self):
        return f"Pago {self.id}"
