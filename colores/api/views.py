from rest_framework.viewsets import ModelViewSet
from colores.models import Colores
from colores.api.serializers import ColoresSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ColoresViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ColoresSerializer
    queryset = Colores.objects.all()
