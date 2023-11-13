from django.contrib import admin
from ventas.models import Ventas

@admin.register(Ventas)

class VentasAdmin(admin.ModelAdmin):
    list_display=['id','comprador','vendedor','fecha_venta']
    
