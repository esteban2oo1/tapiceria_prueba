from rest_framework.routers import DefaultRouter
from .views import VentasProductosViewSet

router_ventasProductos = DefaultRouter()

router_ventasProductos.register(
    prefix='ventasProductos',
    basename='ventasProductos',
    viewset=VentasProductosViewSet
)
