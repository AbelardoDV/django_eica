from django.core import serializers
from django.http import HttpResponse
###########################################################
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
###########################################################
from .models import ProductoHijoCompra
from .models import ProductoPadre
from .models import Proveedor
from .models import BoletaCompra
###########################################################
from .models import ProductoPlato
from .models import PlatoPadre
from .models import PlatoVenta
from .models import BoletaVentaRestaurante

import datetime


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
#Aquí se registran las compras
@login_required(login_url='/accounts/login')
def compras_productos_view(request):

    #Aquí se recoje toda la información a insertar
    if request.method == 'POST':
        
        #Obtener información de la boleta   
        fecha= datetime.datetime.strptime(request.POST.get('fecha_compra'), "%d/%m/%Y")
        id_proveedor=request.POST.get('id_proveedor') #El proveedor es el mismo para todos
        id_boleta_compra = request.POST.get('id_boleta_compra')
        BoletaCompra.objects.create(fecha_compra=fecha)
        
        print(id_boleta_compra)
        
        # ProductoHijoCompra.objects.create(id_proveedor=Proveedor.objects.get(pk=id_proveedor),id_boleta_compra=BoletaCompra.objects.get(pk=id_boleta_compra),id_producto_padre=ProductoPadre.objects.get(pk=id_producto_padre_1),precio=precio_1,cantidad=cantidad_1)
        #Obtener información de los productos
        for key, value in request.POST.items():
            
            
            if "id_producto_padre" in key:   
                id_producto_padre = int(value)
            if "Cantidad" in key:
                cantidad = float(value)
            if "Precio" in key:
                precio = float(value)
                #Solo cuando tenga Precio se agrega, el key y value pues son del producto
                ProductoHijoCompra.objects.create(id_proveedor=Proveedor.objects.get(pk=id_proveedor),id_boleta_compra=BoletaCompra.objects.get(pk=id_boleta_compra),id_producto_padre=ProductoPadre.objects.get(pk=id_producto_padre),precio=precio,cantidad=cantidad)
                
            
            
    else:
        0
        
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


# ---------------------------------Inicio Editar---------------------------------

@login_required(login_url='/accounts/login')
def editar_plato_view(request):
    nombre_vista = 'Editar platos'
    ruta_vista = ['Editar platos']
    
    platoVenta=PlatoVenta.objects.all()
    platoPadre=PlatoPadre.objects.all()
    
    json_platoVenta = serializers.serialize("json", platoVenta)  # Usado para autocompletado
    json_platoPadre = serializers.serialize("json", platoPadre)  # Usado para autocompletado
    
    return render(request, 'editar_platos.html', locals())

# ---------------------------------Fin Editar---------------------------------



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


