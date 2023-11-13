from django.urls import path
from rest_framework.routers import DefaultRouter
from colores.api.views import ColoresViewSet

router_color=DefaultRouter()

router_color.register(
    prefix='colores',
    basename='colores',
    viewset=ColoresViewSet
)