from rest_framework import viewsets
from pagos.models import Pagos
from pagos.api.serializers import PagosSerializer

class PagosViewSet(viewsets.ModelViewSet):
    queryset = Pagos.objects.all()
    serializer_class = PagosSerializer
