from django.contrib import admin
from creditos.models import Creditos

@admin.register(Creditos)
class CreditosAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'total_credito', 'monto_inicial', 'fecha_credito')
