from rest_framework.serializers import ModelSerializer
from telas_colores.models import TelasColores

class TelasColoresSerializer(ModelSerializer):
    class Meta:
        model = TelasColores
        fields = '__all__'