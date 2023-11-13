from rest_framework import serializers
from existenciasEspumillas.models import ExistenciasEspumillas

class ExistenciasEspumillasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExistenciasEspumillas
        fields = '__all__'
