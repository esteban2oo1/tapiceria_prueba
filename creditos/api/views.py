from rest_framework import viewsets
from creditos.models import Creditos
from creditos.api.serializers import CreditosSerializer

class CreditosViewSet(viewsets.ModelViewSet):
    queryset = Creditos.objects.all()
    serializer_class = CreditosSerializer
