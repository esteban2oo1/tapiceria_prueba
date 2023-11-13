from rest_framework import serializers
from detallesTapizados.models import DetallesTapizados

class DetallesTapizadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallesTapizados
        fields = '__all__'