from rest_framework.routers import DefaultRouter
from existenciasTelasColores.api.views import ExistenciasTelasColoresViewSet

router_existenciasTelasColores = DefaultRouter()

router_existenciasTelasColores.register(
    prefix='existencias_telas_colores',
    basename='existencias_telas_colores',
    viewset=ExistenciasTelasColoresViewSet
)
