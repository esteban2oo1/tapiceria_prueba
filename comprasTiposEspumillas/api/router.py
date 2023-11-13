from rest_framework.routers import DefaultRouter
from comprasTiposEspumillas.api.views import ComprasTiposEspumillasViewSet

router_comprasTiposEspumillas = DefaultRouter()

router_comprasTiposEspumillas.register(
    prefix='compras_tipos_espumillas',
    basename='compras_tipos_espumillas',
    viewset=ComprasTiposEspumillasViewSet
)
