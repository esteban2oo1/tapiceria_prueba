from rest_framework.viewsets import ModelViewSet
from tiposMateriales.models import TiposMateriales
from tiposMateriales.api.serializers import TiposMaterialesSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class TiposMaterialesViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = TiposMaterialesSerializer
    queryset = TiposMateriales.objects.all()
