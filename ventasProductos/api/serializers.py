from rest_framework import serializers
from ventasProductos.models import VentasProductos

class VentasProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = VentasProductos
        fields = '__all__'
