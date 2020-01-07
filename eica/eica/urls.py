"""eica URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from eica.views import dashboard_view

from eica.views import ventas_restaurante_view
from eica.views import ventas_bodega_view
from eica.views import ventas_historial_view
from eica.views import compras_productos_view
from eica.views import compras_historial_view
from eica.views import agregar_plato_view

from eica.views import error_404_view
from eica.views import error_500_view

urlpatterns = [
    path('', dashboard_view, name='login'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('dashboard/', dashboard_view, name='dashboard'),

    # -----------------Inicio páginas por defecto-----------------

    path("404/", error_404_view),
    path("500/", error_500_view),

    # -----------------Fin páginas por defecto-----------------

    # -----------------Inicio seccion de ventas-----------------
    path('ventas_restaurante/', ventas_restaurante_view, name='ventas_restaurante'),
    path('ventas_bodega/', ventas_bodega_view, name='ventas_bodega'),
    path('ventas_historial/', ventas_historial_view, name='ventas_historial'),
    # -----------------Fin seccion de ventas-----------------


    # -----------------Inicio seccion de Compra-----------------
    path('compras_productos/', compras_productos_view, name='compras_productos'),
    path('compras_historial/', compras_historial_view, name='compras_historial'),
    # -----------------Inicio seccion de Compra-----------------

    # -----------------Inicio seccion agregar plato-----------------
    path('agregar_plato/', agregar_plato_view, name='agregar_plato'),
    # -----------------Fin seccion agregar plato-----------------


]
