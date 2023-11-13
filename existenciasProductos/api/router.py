from rest_framework.routers import DefaultRouter
from existenciasProductos.api.views import ExistenciasProductosViewSet

router_existenciasProductos = DefaultRouter()

router_existenciasProductos.register(
    prefix='existencias_productos',
    basename='existencias_productos',
    viewset=ExistenciasProductosViewSet
)
