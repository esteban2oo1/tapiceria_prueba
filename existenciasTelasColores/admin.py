from django.contrib import admin
from existenciasTelasColores.models import ExistenciasTelasColores

@admin.register(ExistenciasTelasColores)
class ExistenciasTelasColoresAdmin(admin.ModelAdmin):
    list_display = ('id', 'tela_Color', 'cantidad')
