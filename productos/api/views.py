from rest_framework.viewsets import ModelViewSet
from productos.models import Productos 
from productos.api.serializers import ProductosSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ProductosViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ProductosSerializer
    queryset = Productos.objects.all()