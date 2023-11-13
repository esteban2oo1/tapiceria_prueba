from django.contrib import admin
from comprasTiposMateriales.models import ComprasTiposMateriales

@admin.register(ComprasTiposMateriales)
class ComprasTiposMaterialesAdmin(admin.ModelAdmin):
    pass
