from rest_framework.serializers import ModelSerializer, SerializerMethodField
from productos.models import Productos
from tiposMateriales.models import TiposMateriales
from tiposProductos.models import TiposProductos

class ProductosSerializer(ModelSerializer):
    tipoMaterial_data = SerializerMethodField()
    tipoProducto_data = SerializerMethodField()

    class Meta:
        model = Productos
        fields = '__all__'

    def get_tipoMaterial_data(self, obj):
        tipo_material = obj.tipoMaterial
        return {'id': tipo_material.id, 'nombre': tipo_material.nombre} if tipo_material else None

    def get_tipoProducto_data(self, obj):
        tipo_producto = obj.tipoProducto
        return {'id': tipo_producto.id, 'nombre': tipo_producto.nombre} if tipo_producto else None
