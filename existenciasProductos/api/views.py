from rest_framework import viewsets
from existenciasProductos.models import ExistenciasProductos
from existenciasProductos.api.serializers import ExistenciasProductosSerializer

class ExistenciasProductosViewSet(viewsets.ModelViewSet):
    queryset = ExistenciasProductos.objects.all()
    serializer_class = ExistenciasProductosSerializer
