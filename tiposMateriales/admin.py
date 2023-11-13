from django.contrib import admin
from tiposMateriales.models import TiposMateriales

@admin.register(TiposMateriales)

class TiposMaterialesAdmin(admin.ModelAdmin):
    list_display=['id','nombre']
    
