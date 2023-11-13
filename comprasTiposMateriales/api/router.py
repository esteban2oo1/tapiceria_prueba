from rest_framework.routers import DefaultRouter
from comprasTiposMateriales.api.views import ComprasTiposMaterialesViewSet

router_comprasTiposMateriales = DefaultRouter()

router_comprasTiposMateriales.register(
    prefix='compras_tipos_materiales',
    basename='compras_tipos_materiales',
    viewset=ComprasTiposMaterialesViewSet
)
