from rest_framework import viewsets
from existenciasMateriales.models import ExistenciasMateriales
from existenciasMateriales.api.serializers import ExistenciasMaterialesSerializer

class ExistenciasMaterialesViewSet(viewsets.ModelViewSet):
    queryset = ExistenciasMateriales.objects.all()
    serializer_class = ExistenciasMaterialesSerializer
