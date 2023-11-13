from django.contrib import admin
from existenciasMateriales.models import ExistenciasMateriales

@admin.register(ExistenciasMateriales)
class ExistenciasMaterialesAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipoMaterial', 'cantidad')
