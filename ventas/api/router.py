from rest_framework.routers import DefaultRouter
from ventas.api.views import VentasViewSet

router_ventas = DefaultRouter()

router_ventas.register(
    prefix='ventas',
    basename='ventas',
    viewset=VentasViewSet
)
