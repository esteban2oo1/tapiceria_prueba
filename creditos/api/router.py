from rest_framework.routers import DefaultRouter
from creditos.api.views import CreditosViewSet

router_creditos = DefaultRouter()

router_creditos.register(
    prefix='creditos',
    basename='creditos',
    viewset=CreditosViewSet
)
