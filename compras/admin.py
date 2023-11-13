from django.contrib import admin
from .models import Compras

@admin.register(Compras)
class ComprasAdmin(admin.ModelAdmin):
    list_display=['id','comprador','proveedor','fecha_compra']
