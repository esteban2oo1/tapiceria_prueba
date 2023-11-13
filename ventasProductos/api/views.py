from rest_framework import viewsets
from ventasProductos.models import VentasProductos
from ventasProductos.api.serializers import VentasProductosSerializer

class VentasProductosViewSet(viewsets.ModelViewSet):
    queryset = VentasProductos.objects.all()
    serializer_class = VentasProductosSerializer
