from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from alimentos.views import alimentos_list, alimentos_detail
from bebidas.views import list_bebidas, retrieve_bebida
from caja.views import list_caja, retrieve_caja
from pedidos.views import list_pedidos, retrieve_pedidos
from usuarios.views import list_usuarios, retrieve_usuario, protected_resource

urlpatterns = [
    path('admin/', admin.site.urls),  # URL para el panel de administración de Django
    
    # Rutas para vistas asíncronas basadas en funciones - alimentos
    path('alimentos/', alimentos_list, name='alimentos-list'),  # GET, POST
    path('alimentos/<int:pk>/', alimentos_detail, name='alimentos-detail'),  # GET, PUT, PATCH, DELETE
    
    # Rutas para vistas asíncronas basadas en funciones - bebidas
    path('bebidas/', list_bebidas, name='list_bebidas'),  # GET, POST
    path('bebidas/<int:pk>/', retrieve_bebida, name='retrieve_bebida'),  # GET, PUT, PATCH, DELETE

    # Rutas para vistas asíncronas basadas en funciones - caja
    path('caja/', list_caja, name='list_caja'),  # GET, POST
    path('caja/<int:pk>/', retrieve_caja, name='retrieve_caja'),  # GET, PUT, PATCH, DELETE

    # Rutas para vistas asíncronas basadas en funciones - pedidos
    path('pedidos/', list_pedidos, name='list_pedidos'),  # GET, POST
    path('pedidos/<int:pk>/', retrieve_pedidos, name='retrieve_pedidos'),  # GET, PUT, PATCH, DELETE

    # Rutas para vistas asíncronas basadas en funciones - usuarios
    path('usuarios/', list_usuarios, name='list_usuarios'),  # GET, POST
    path('usuarios/<int:pk>/', retrieve_usuario, name='retrieve_usuario'),  # GET, PUT, PATCH, DELETE

    # Rutas para la autenticación JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Rutas protegidas por JWT
    path('api/protected-resource/', protected_resource, name='protected_resource'),
]
