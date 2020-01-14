from django.core import serializers
from django.http import HttpResponse
# from eica.models import Personas
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ProductoHijoCompra
from .models import ProductoPadre
from .models import Proveedor
from .models import BoletaCompra

from .models import ProductoPlato
from .models import PlatoPadre
from .models import PlatoVenta
from .models import BoletaVentaRestaurante

# -------------------------Inicio Dashboard-------------------------


@login_required(login_url='/accounts/login')
def dashboard_view(request):
    nombre_vista = 'Dashboard'
    ruta_vista = ['Dashboard']
    return render(request, 'dashboard.html', locals())

# ---------------------------Fin Dashboard-------------------------


# ---------------------------------Inicio Seccion Ventas---------------------------------

# Ventas de restaurante
@login_required(login_url='/accounts/login')
def ventas_restaurante_view(request):
    nombre_vista = 'Ventas de Restaurante'
    ruta_vista = ['Ventas de Restaurante']
    
    productoPlato=ProductoPlato.objects.all()
    platoPadre=PlatoPadre.objects.all()
    platoVenta=PlatoVenta.objects.all()
    boletaVentaRestaurante=BoletaVentaRestaurante.objects.all()
    productoPadre = ProductoPadre.objects.all()
    

    json_productoPlato = serializers.serialize("json", productoPlato)  # Usado para autocompletado
    json_platoPadre = serializers.serialize("json", platoPadre)  # Usado para autocompletado
    json_platoVenta = serializers.serialize("json", platoVenta)  # Usado para autocompletado
    json_boletaVentaRestaurante = serializers.serialize("json", boletaVentaRestaurante)  # Usado para autocompletado
    json_productoPadre = serializers.serialize("json", productoPadre)  # Usado para autocompletado

    
    return render(request, 'ventas_restaurante.html', locals())

# Ventas de bodega
@login_required(login_url='/accounts/login')
def ventas_bodega_view(request):
    nombre_vista = 'Ventas de Bodega'
    ruta_vista = ['Ventas de Bodega']
    return render(request, 'ventas_bodega.html', locals())

# Historial de Ventas
@login_required(login_url='/accounts/login')
def ventas_historial_view(request):
    nombre_vista = 'Historial de Ventas'
    ruta_vista = ['Historial de Ventas']
    return render(request, 'ventas_historial.html', locals())


# ---------------------------------Fin Seccion Ventas---------------------------------

# ---------------------------------Inicio Seccion Productos---------------------------------
@login_required(login_url='/accounts/login')
def compras_productos_view(request):
    nombre_vista = 'Compras de Productos'
    ruta_vista = ['Compras de Productos']
    
    proveedores = Proveedor.objects.all()
    productoHijoCompra = ProductoHijoCompra.objects.all()
    productoPadre = ProductoPadre.objects.all()
    boletasCompra = BoletaCompra.objects.all()

    json_proveedores = serializers.serialize("json", proveedores)  # Usado para autocompletado
    json_producto_hijo = serializers.serialize("json", productoHijoCompra)  # Usado para autocompletado
    json_producto_padre = serializers.serialize("json", productoPadre)  # Usado para autocompletado

    return render(request, 'compras_productos.html', locals())


@login_required(login_url='/accounts/login')
def compras_historial_view(request):
    nombre_vista = 'Compras Historial'
    ruta_vista = ['Compras Historial']
    return render(request, 'compras_historial.html', locals())

# ---------------------------------Fin Seccion Productos---------------------------------


# ------------------------------Inicio Seccion Agregar---------------------------------
@login_required(login_url='/accounts/login')
def agregar_plato_view(request):
    nombre_vista = 'Agregar plato'
    ruta_vista = ['Agregar plato']
    return render(request, 'agregar_plato.html', locals())

# ------------------------------Fin Seccion Agregar---------------------------------

# ---------------------------Inicio Páginas 404 y 500---------------------------


def error_404_view(request, exception):
    data = {"example": "text.com"}
    return render(request, 'eica/404.html', data)


def error_500_view(request, exception):
    data = {"example": "text.com"}
    return render(request, 'eica/500.html', data)

# ---------------------------Fin Páginas 404 y 500---------------------------
