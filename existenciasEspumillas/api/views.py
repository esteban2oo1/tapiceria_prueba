from rest_framework import viewsets
from existenciasEspumillas.models import ExistenciasEspumillas
from existenciasEspumillas.api.serializers import ExistenciasEspumillasSerializer

class ExistenciasEspumillasViewSet(viewsets.ModelViewSet):
    queryset = ExistenciasEspumillas.objects.all()
    serializer_class = ExistenciasEspumillasSerializer
