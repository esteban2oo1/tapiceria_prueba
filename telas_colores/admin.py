from django.contrib import admin
from telas_colores.models import TelasColores


@admin.register(TelasColores)

class TelasColores(admin.ModelAdmin):
    list_display=['id','tela','color']
    
