from rest_framework.viewsets import ModelViewSet
from tiposTelas.models import TiposTelas
from tiposTelas.api.serializers import TiposTelasSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class TiposTelasViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = TiposTelasSerializer
    queryset = TiposTelas.objects.all()
