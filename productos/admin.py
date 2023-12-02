from django.contrib import admin
from productos.models import Productos

@admin.register(Productos)

class ProductosAdmin(admin.ModelAdmin):
    list_display=['id','imagen','descripcion','tipoProducto','tipoMaterial','fecha_fabricacion','precio_costo','precio_venta']
