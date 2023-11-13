from rest_framework.serializers import ModelSerializer
from colores.models import Colores

class ColoresSerializer(ModelSerializer):
    class Meta:
        model = Colores
        fields = ['id', 'nombre']
