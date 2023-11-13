from django.contrib import admin
from existenciasProductos.models import ExistenciasProductos

@admin.register(ExistenciasProductos)
class ExistenciasProductosAdmin(admin.ModelAdmin):
    list_display = ('id', 'producto', 'cantidad')
