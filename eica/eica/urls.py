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
from eica.views import dashboard_reporte_economico_view

from eica.views import ventas_restaurante_view
from eica.views import ventas_bodega_view
from eica.views import ventas_historial_view
from eica.views import actualizar_boletaVentaRestaurante_valido

from eica.views import compras_productos_view
from eica.views import compras_historial_boletas_view
from eica.views import compras_historial_productos_view
from eica.views import compra_producto_cantidad_real
from eica.views import actualizar_boletaCompra_valido_ajax
from eica.views import reporte_economico_ajax

from eica.views import inventario_productos_view

from eica.views import editar_plato_view

from eica.views import enviar_cocina

from eica.views import error_404_view
from eica.views import error_500_view


urlpatterns = [

    path('', dashboard_view, name='login'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    # -----------------Inicio Dashboard --------------------------
    path('dashboard/', dashboard_view, name='dashboard'),
    path('dashboard/reporte_economico', dashboard_reporte_economico_view, name='reporte_economico'),

    # -----------------Fin Dashboard ----------------------------

    # -----------------Inicio páginas por defecto-----------------
    path("404/", error_404_view),
    path("500/", error_500_view),
    # -----------------Fin páginas por defecto-----------------

    # -----------------Inicio seccion de ventas-----------------
    path('ventas_restaurante/', ventas_restaurante_view, name='ventas_restaurante'),
    path('ventas_bodega/', ventas_bodega_view, name='ventas_bodega'),
    path('ventas_historial/', ventas_historial_view, name='ventas_historial'),
    path('ventas/actualizar_valido/', actualizar_boletaVentaRestaurante_valido, name='actualizar_valido'),
    # -----------------Fin seccion de ventas-----------------


    # -----------------Inicio seccion de Compra-----------------
    path('compras_productos/', compras_productos_view, name='compras_productos'),
    path('compras_historial_boletas/', compras_historial_boletas_view, name='compras_historial_boletas'),
    path('compras_historial_productos/', compras_historial_productos_view, name='compras_historial_productos'),
    path('compras_historial_productos/actualizar_cantidad_real/', compra_producto_cantidad_real, name='compras_productos_cantidad_real'),
    path('compras/actualizar_valido/', actualizar_boletaCompra_valido_ajax, name='actualizar_valido'),
    # -----------------Fin seccion de Compra-----------------
    
    #----------------------------Reporte Económico ------------------------
    path('dashboard/reporte_economico/reporte_economico_ajax/', reporte_economico_ajax, name='importe_fecha_rango'),
    path('dashboard/reporte_economico/enviar_cocina/', enviar_cocina, name='enviar_cocina'),
    #----------------------------Fin Reporte Económico----------------------
      
    
    # -----------------Inicio seccion Inventario-----------------
    path('inventario/inventario_productos/', inventario_productos_view, name='inventario_productos'),
    # -----------------Fin seccion Inventario-----------------
    

    # -----------------Inicio seccion agregar plato-----------------
    path('editar_platos/', editar_plato_view, name='editar_platos'),
    # -----------------Fin seccion agregar plato-----------------


    # API
    path('', include('api.urls'))

    # API
]
