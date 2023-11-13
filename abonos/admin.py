from django.contrib import admin
from abonos.models import Abonos

@admin.register(Abonos)
class AbonosAdmin(admin.ModelAdmin):
    list_display = ('id', 'credito', 'monto', 'fecha_abono')
