from django.db import models
from tiposMateriales.models import TiposMateriales
from tiposProductos.models import TiposProductos

class Productos(models.Model):
    imagen= models.ImageField(upload_to='producto', null=True)
    descripcion = models.CharField(max_length=45, null=True)
    tipoProducto = models.ForeignKey(TiposProductos, on_delete=models.CASCADE)
    tipoMaterial = models.ForeignKey(TiposMateriales, on_delete=models.CASCADE)
    fecha_fabricacion = models.DateField(null=True)
    precio_costo = models.IntegerField()
    precio_venta = models.IntegerField()

    def __str__(self):
        return self.descripcion