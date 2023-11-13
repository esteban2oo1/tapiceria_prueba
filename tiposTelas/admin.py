from django.contrib import admin
from tiposTelas.models import TiposTelas


@admin.register(TiposTelas)

class TiposTelas(admin.ModelAdmin):
    list_display=['id','nombre']
    
