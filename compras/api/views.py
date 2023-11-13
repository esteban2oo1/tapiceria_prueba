from rest_framework import viewsets
from compras.models import Compras
from compras.api.serializers import ComprasSerializer

class ComprasViewSet(viewsets.ModelViewSet):
    queryset = Compras.objects.all()
    serializer_class = ComprasSerializer
