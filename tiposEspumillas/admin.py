from django.contrib import admin
from tiposEspumillas.models import TiposEspumillas

@admin.register(TiposEspumillas)

class TiposEspumillasAdmin(admin.ModelAdmin):
    list_display=['id','nombre']
    
