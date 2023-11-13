from rest_framework.routers import DefaultRouter
from tiposEspumillas.api.views import TiposEspumillasViewSet

router_tipos_espumillas = DefaultRouter()

router_tipos_espumillas.register(
    prefix='tipos_espumillas',
    basename='tipos_espumillas',
    viewset=TiposEspumillasViewSet
)