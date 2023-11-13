from django.contrib import admin
from colores.models import Colores

@admin.register(Colores)

class ColoresAdmin(admin.ModelAdmin):
    list_display=['id','nombre']    
    
