from rest_framework import serializers
from existenciasTelasColores.models import ExistenciasTelasColores

class ExistenciasTelasColoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExistenciasTelasColores
        fields = '__all__'
