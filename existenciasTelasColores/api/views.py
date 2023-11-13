from rest_framework import viewsets
from existenciasTelasColores.models import ExistenciasTelasColores
from existenciasTelasColores.api.serializers import ExistenciasTelasColoresSerializer

class ExistenciasTelasColoresViewSet(viewsets.ModelViewSet):
    queryset = ExistenciasTelasColores.objects.all()
    serializer_class = ExistenciasTelasColoresSerializer
