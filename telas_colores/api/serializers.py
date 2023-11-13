from rest_framework.serializers import ModelSerializer, SerializerMethodField
from telas_colores.models import TelasColores
from tiposTelas.models import TiposTelas
from colores.models import Colores

class TelasColoresSerializer(ModelSerializer):
    tela_data = SerializerMethodField()
    color_data = SerializerMethodField()

    class Meta:
        model = TelasColores
        fields = ['id', 'tela_id', 'color_id', 'tela_data', 'color_data']

    def get_tela_data(self, obj):
        tela = obj.tela
        return {'id': tela.id, 'nombre': tela.nombre} if tela else None

    def get_color_data(self, obj):
        color = obj.color
        return {'id': color.id, 'nombre': color.nombre} if color else None
