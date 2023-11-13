from django.contrib import admin
from .models import VentasProductos

@admin.register(VentasProductos)
class VentasProductosAdmin(admin.ModelAdmin):
    list_display = ('id', 'venta', 'producto', 'cantidad')
