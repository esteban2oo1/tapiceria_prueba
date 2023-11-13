from rest_framework.serializers import ModelSerializer
from tiposEspumillas.models import TiposEspumillas

class TiposEspumillasSerializer(ModelSerializer):
    class Meta:
        model = TiposEspumillas
        fields = ['id', 'nombre']