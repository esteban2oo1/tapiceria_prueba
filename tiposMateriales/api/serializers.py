from rest_framework.serializers import ModelSerializer
from tiposMateriales.models import TiposMateriales

class TiposMaterialesSerializer(ModelSerializer):
    class Meta:
        model = TiposMateriales
        fields = ['id', 'nombre']
