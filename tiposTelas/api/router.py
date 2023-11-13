from django.urls import path
from rest_framework.routers import DefaultRouter
from tiposTelas.api.views import TiposTelasViewSet

router_tiposTelas=DefaultRouter()

router_tiposTelas.register(
    prefix='tiposTelas',basename='tiposTelas',viewset=TiposTelasViewSet
)