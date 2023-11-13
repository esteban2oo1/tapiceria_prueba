from rest_framework.viewsets import ModelViewSet
from tiposProductos.models import TiposProductos
from tiposProductos.api.serializers import TiposProductosSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class TiposProductosViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = TiposProductosSerializer
    queryset = TiposProductos.objects.all()
