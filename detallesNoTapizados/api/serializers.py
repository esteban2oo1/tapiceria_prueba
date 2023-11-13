from rest_framework import serializers
from detallesNoTapizados.models import DetallesNoTapizados

class DetallesNoTapizadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallesNoTapizados
        fields = '__all__'