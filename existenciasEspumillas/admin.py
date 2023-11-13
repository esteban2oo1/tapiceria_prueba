from django.contrib import admin
from existenciasEspumillas.models import ExistenciasEspumillas

@admin.register(ExistenciasEspumillas)
class ExistenciasEspumillasAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipoEspumilla', 'cantidad')
