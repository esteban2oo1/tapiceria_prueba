from rest_framework import viewsets
from comprasTiposEspumillas.models import ComprasTiposEspumillas
from comprasTiposEspumillas.api.serializers import ComprasTiposEspumillasSerializer

class ComprasTiposEspumillasViewSet(viewsets.ModelViewSet):
    queryset = ComprasTiposEspumillas.objects.all()
    serializer_class = ComprasTiposEspumillasSerializer
