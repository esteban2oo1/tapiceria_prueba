from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from users.api.router import route_user
from colores.api.router import router_color
from tiposTelas.api.router import router_tiposTelas
from telas_colores.api.router import router_telas_colores
from tiposEspumillas.api.router import router_tipos_espumillas
from tiposProductos.api.router import router_tiposProductos
from tiposMateriales.api.router import router_tiposMateriales
from productos.api.router import router_productos
from detallesTapizados.api.router import router_detallesTapizados
from detallesNoTapizados.api.router import router_detallesNoTapizados
from ventas.api.router import router_ventas
from ventasProductos.api.router import router_ventasProductos
from compras.api.router import router_compras
from comprasTelasColores.api.router import router_comprasTelasColores
from comprasTiposEspumillas.api.router import router_comprasTiposEspumillas
from comprasTiposMateriales.api.router import router_comprasTiposMateriales
from existenciasTelasColores.api.router import router_existenciasTelasColores
from existenciasEspumillas.api.router import router_existenciasEspumillas
from existenciasMateriales.api.router import router_existenciasMateriales
from existenciasProductos.api.router import router_existenciasProductos
from pagos.api.router import router_pagos
from creditos.api.router import router_creditos
from abonos.api.router import router_abonos
from users.api.router import router_groups
from .views import load_image

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth.views import LogoutView, LoginView

schema_view = get_schema_view(
   openapi.Info(
      title="API Tapiceria",
      default_version='v1',
      description="Documentación Api Tapiceria",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="maycolguerrero2021@itp.edu.co"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
from users.models import User

urlpatterns = [
   path('admin/', admin.site.urls),
   path('documentacionapi<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('documentacionapi/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path('api', include('users.api.router')),
   path('api', include(route_user.urls)),
   path('api', include(router_color.urls)),
   path('api', include(router_tiposTelas.urls)),
   path('api', include(router_telas_colores.urls)),
   path('api', include(router_tipos_espumillas.urls)),
   path('api', include(router_tiposProductos.urls)),
   path('api', include(router_tiposMateriales.urls)),
   path('api', include(router_productos.urls)),
   path('api', include(router_detallesTapizados.urls)),
   path('api', include(router_detallesNoTapizados.urls)),
   path('api', include(router_ventas.urls)),
   path('api', include(router_ventasProductos.urls)),
   path('api', include(router_compras.urls)),
   path('api', include(router_comprasTelasColores.urls)),
   path('api', include(router_comprasTiposEspumillas.urls)),
   path('api', include(router_comprasTiposMateriales.urls)),
   path('api', include(router_existenciasTelasColores.urls)),
   path('api', include(router_existenciasEspumillas.urls)),
   path('api', include(router_existenciasMateriales.urls)),
   path('api', include(router_existenciasProductos.urls)),
   path('api', include(router_pagos.urls)),
   path('api', include(router_creditos.urls)),
   path('api', include(router_abonos.urls)),
   path('api', include(router_groups.urls)),
   path('api/token/',TokenObtainPairView.as_view(),name="TokenObtainPairView"),
   path('api/token/refresh/', TokenRefreshView.as_view(), name='TokenRefreshView'),
   path('accounts/login/', LoginView.as_view(), name='login'),
   path('accounts/logout/', LogoutView.as_view(), name='logout'),
   path('imagenes/producto/<str:image_name>/', load_image, name='load_image'),
   path('imagenes/producto/<str:image_name>', load_image),
] + static(settings.STATIC_URL, documet_root=settings.STATIC_ROOT)

