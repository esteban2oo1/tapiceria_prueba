from django.contrib import admin
from comprasTiposEspumillas.models import ComprasTiposEspumillas

@admin.register(ComprasTiposEspumillas)
class ComprasTiposEspumillasAdmin(admin.ModelAdmin):
    list_display=['id','compra','tipoEspumilla','precio','cantidad']