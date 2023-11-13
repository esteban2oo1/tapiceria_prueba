from django.contrib import admin
from .models import ComprasTelasColores

@admin.register(ComprasTelasColores)
class ComprasTelasColoresAdmin(admin.ModelAdmin):
    list_display=['id','compra','tela_color','precio','cantidad']