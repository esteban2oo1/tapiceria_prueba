from rest_framework.routers import DefaultRouter
from existenciasEspumillas.api.views import ExistenciasEspumillasViewSet

router_existenciasEspumillas = DefaultRouter()

router_existenciasEspumillas.register(
    prefix='existencias_espumillas',
    basename='existencias_espumillas',
    viewset=ExistenciasEspumillasViewSet
)
