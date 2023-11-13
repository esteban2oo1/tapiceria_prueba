from django.contrib import admin
from detallesTapizados.models import DetallesTapizados

@admin.register(DetallesTapizados)

class DetallesTapizadosAdmin(admin.ModelAdmin):
    list_display=['id','tipoTela','color','producto','tipoEspumilla','cantidad_telasColores','cantidad_tipoMaterial']
    
