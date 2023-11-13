from rest_framework import serializers
from comprasTiposMateriales.models import ComprasTiposMateriales

class ComprasTiposMaterialesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComprasTiposMateriales
        fields = '__all__'
