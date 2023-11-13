from rest_framework import serializers
from comprasTiposEspumillas.models import ComprasTiposEspumillas

class ComprasTiposEspumillasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComprasTiposEspumillas
        fields = '__all__'
