# detallesNoTapizados/api/views.py
from rest_framework import viewsets
from detallesNoTapizados.models import DetallesNoTapizados
from detallesNoTapizados.api.serializers import DetallesNoTapizadosSerializer

class DetallesNoTapizadosViewSet(viewsets.ModelViewSet):
    queryset = DetallesNoTapizados.objects.all()
    serializer_class = DetallesNoTapizadosSerializer
