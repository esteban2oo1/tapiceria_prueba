from rest_framework import viewsets
from comprasTelasColores.models import ComprasTelasColores
from comprasTelasColores.api.serializers import ComprasTelasColoresSerializer

class ComprasTelasColoresViewSet(viewsets.ModelViewSet):
    queryset = ComprasTelasColores.objects.all()
    serializer_class = ComprasTelasColoresSerializer
