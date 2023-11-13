from rest_framework.routers import DefaultRouter
from abonos.api.views import AbonosViewSet

router_abonos = DefaultRouter()

router_abonos.register(
    prefix='abonos',
    basename='abonos',
    viewset=AbonosViewSet
)
