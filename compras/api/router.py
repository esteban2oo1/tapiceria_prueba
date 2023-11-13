from rest_framework.routers import DefaultRouter
from compras.api.views import ComprasViewSet

router_compras = DefaultRouter()

router_compras.register(
    prefix='compras',
    basename='compras',
    viewset=ComprasViewSet
)
