from rest_framework.viewsets import ModelViewSet
from telas_colores.models import TelasColores
from telas_colores.api.serializers import TelasColoresSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class TelasColoresViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = TelasColoresSerializer
    queryset = TelasColores.objects.all()
