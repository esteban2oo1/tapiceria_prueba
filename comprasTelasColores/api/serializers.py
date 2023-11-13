from rest_framework import serializers
from comprasTelasColores.models import ComprasTelasColores

class ComprasTelasColoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComprasTelasColores
        fields = '__all__'
