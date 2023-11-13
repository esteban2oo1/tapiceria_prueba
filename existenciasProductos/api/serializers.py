from rest_framework import serializers
from existenciasProductos.models import ExistenciasProductos

class ExistenciasProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExistenciasProductos
        fields = '__all__'
