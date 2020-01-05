from django.http import HttpResponse
# from eica.models import Personas
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# ---------------------------Inicio Páginas 404 y 500---------------------------

def error_404_view(request, exception):
    data = {"example": "text.com"}
    return render(request, 'eica/404.html', data)

def error_500_view(request, exception):
    data = {"example": "text.com"}
    return render(request, 'eica/500.html', data)

# ---------------------------Fin Páginas 404 y 500---------------------------

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
    return render(request, 'compras_productos.html', locals())


@login_required(login_url='/accounts/login')
def compras_historial_view(request):
    nombre_vista = 'Compras Historial'
    ruta_vista = ['Compras Historial']
    return render(request, 'compras_historial.html', locals())

# ---------------------------------Fin Seccion Productos---------------------------------
