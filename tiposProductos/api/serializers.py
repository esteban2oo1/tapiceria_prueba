from rest_framework.serializers import ModelSerializer
from tiposProductos.models import TiposProductos

class TiposProductosSerializer(ModelSerializer):
    class Meta:
        model = TiposProductos
        fields = ['id', 'nombre']
