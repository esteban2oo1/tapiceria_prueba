from rest_framework import serializers
from existenciasMateriales.models import ExistenciasMateriales

class ExistenciasMaterialesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExistenciasMateriales
        fields = '__all__'
