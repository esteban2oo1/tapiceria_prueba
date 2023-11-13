from rest_framework.routers import DefaultRouter
from telas_colores.api.views import TelasColoresViewSet

router_telas_colores=DefaultRouter()

router_telas_colores.register(
    prefix='telas_colores',
    basename='telas_colores',
    viewset=TelasColoresViewSet
)