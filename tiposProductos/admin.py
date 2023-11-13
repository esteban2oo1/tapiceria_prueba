from django.contrib import admin
from tiposProductos.models import TiposProductos

@admin.register(TiposProductos)

class TiposProductosAdmin(admin.ModelAdmin):
    list_display=['id','nombre']
    
