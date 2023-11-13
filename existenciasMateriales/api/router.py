from rest_framework.routers import DefaultRouter
from existenciasMateriales.api.views import ExistenciasMaterialesViewSet

router_existenciasMateriales = DefaultRouter()

router_existenciasMateriales.register(
    prefix='existencias_materiales',
    basename='existencias_materiales',
    viewset=ExistenciasMaterialesViewSet
)
