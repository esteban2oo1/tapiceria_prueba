from rest_framework.viewsets import ModelViewSet
from tiposEspumillas.models import TiposEspumillas
from tiposEspumillas.api.serializers import TiposEspumillasSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class TiposEspumillasViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = TiposEspumillasSerializer
    queryset = TiposEspumillas.objects.all()