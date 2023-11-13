from django.contrib import admin
from detallesNoTapizados.models import DetallesNoTapizados

@admin.register(DetallesNoTapizados)

class DetallesNoTapizadosAdmin(admin.ModelAdmin):
    list_display=['id','color','producto']    
