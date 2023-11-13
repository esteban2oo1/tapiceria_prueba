from rest_framework.routers import DefaultRouter
from pagos.api.views import PagosViewSet

router_pagos = DefaultRouter()

router_pagos.register(
    prefix='pagos',
    basename='pagos',
    viewset=PagosViewSet
)
