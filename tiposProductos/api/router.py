from rest_framework.routers import DefaultRouter
from tiposProductos.api.views import TiposProductosViewSet

router_tiposProductos = DefaultRouter()
router_tiposProductos.register(
    prefix='tipos_productos',
    basename='tipos_productos',
    viewset=TiposProductosViewSet
)
