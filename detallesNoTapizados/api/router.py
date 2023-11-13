from django.urls import path
from rest_framework.routers import DefaultRouter
from detallesNoTapizados.api.views import DetallesNoTapizadosViewSet

router_detallesNoTapizados=DefaultRouter()

router_detallesNoTapizados.register(
    prefix='detallesNoTapizados',
    basename='detallesNoTapizados',
    viewset=DetallesNoTapizadosViewSet
)