from django.urls import path
from rest_framework.routers import DefaultRouter
from detallesTapizados.api.views import DetallesTapizadosViewSet

router_detallesTapizados=DefaultRouter()

router_detallesTapizados.register(
    prefix='detallesTapizados',
    basename='detallesTapizados',
    viewset=DetallesTapizadosViewSet
)