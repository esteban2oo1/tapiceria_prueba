from rest_framework.serializers import ModelSerializer
from tiposTelas.models import TiposTelas

class TiposTelasSerializer(ModelSerializer):
    class Meta:
        model = TiposTelas
        fields = ['id', 'nombre']
