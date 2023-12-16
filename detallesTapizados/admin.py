from django.contrib import admin
from detallesTapizados.models import DetallesTapizados

@admin.register(DetallesTapizados)
class DetallesTapizadosAdmin(admin.ModelAdmin):
    list_display=['id','tipoTela','color','tipoEspumilla','tipoMaterial', 'producto', 'cantidad_telaColor', 'cantidad_tipoEspumilla', 'cantidad_tipoMaterial','cantidad_producto']