from rest_framework.routers import DefaultRouter
from productos.api.views import ProductosViewSet

router_productos = DefaultRouter()
router_productos.register(
    prefix='productos',
    basename='productos',
    viewset=ProductosViewSet
)
