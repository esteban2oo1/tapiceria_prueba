from django.contrib import admin
from pagos.models import Pagos

@admin.register(Pagos)
class PagosAdmin(admin.ModelAdmin):
    list_display = ('id', 'monto', 'fecha_pago', 'ventaProducto')
