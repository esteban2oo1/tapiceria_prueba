from django.contrib import admin
from detallesNoTapizados.models import DetallesNoTapizados

@admin.register(DetallesNoTapizados)
class DetallesNoTapizadosAdmin(admin.ModelAdmin):
    list_display = ['id', 'color', 'tipoMaterial', 'producto', 'cantidad_producto', 'cantidad_tipoMaterial', 'cantidad_producto']