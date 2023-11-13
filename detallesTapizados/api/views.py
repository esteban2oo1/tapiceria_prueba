from rest_framework import viewsets
from detallesTapizados.models import DetallesTapizados
from detallesTapizados.api.serializers import DetallesTapizadosSerializer

class DetallesTapizadosViewSet(viewsets.ModelViewSet):
    queryset = DetallesTapizados.objects.all()
    serializer_class = DetallesTapizadosSerializer