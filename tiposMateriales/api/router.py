from rest_framework.routers import DefaultRouter
from tiposMateriales.api.views import TiposMaterialesViewSet

router_tiposMateriales = DefaultRouter()
router_tiposMateriales.register(
    prefix='tipos_materiales',
    basename='tipos_materiales',
    viewset=TiposMaterialesViewSet
)
