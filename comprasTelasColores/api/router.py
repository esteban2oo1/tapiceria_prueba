from rest_framework.routers import DefaultRouter
from comprasTelasColores.api.views import ComprasTelasColoresViewSet

router_comprasTelasColores = DefaultRouter()

router_comprasTelasColores.register(
    prefix='compras_telas_colores',
    basename='compras_telas_colores',
    viewset=ComprasTelasColoresViewSet
)
