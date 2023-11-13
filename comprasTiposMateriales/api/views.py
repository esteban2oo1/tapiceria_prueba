from rest_framework import viewsets
from comprasTiposMateriales.models import ComprasTiposMateriales
from comprasTiposMateriales.api.serializers import ComprasTiposMaterialesSerializer

class ComprasTiposMaterialesViewSet(viewsets.ModelViewSet):
    queryset = ComprasTiposMateriales.objects.all()
    serializer_class = ComprasTiposMaterialesSerializer
