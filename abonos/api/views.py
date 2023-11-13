from rest_framework import viewsets
from abonos.models import Abonos
from abonos.api.serializers import AbonosSerializer

class AbonosViewSet(viewsets.ModelViewSet):
    queryset = Abonos.objects.all()
    serializer_class = AbonosSerializer
