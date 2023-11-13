from django.db import models
from ventas.models import Ventas
from productos.models import Productos

class VentasProductos(models.Model):
    venta = models.ForeignKey(Ventas, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"VentaProducto {self.id}"
