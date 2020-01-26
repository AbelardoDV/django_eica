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
from .models import PlatoHijoVenta
from .models import BoletaVentaRestaurante
from .models import Proveedor

import datetime

# -------------------------Inicio Dashboard-------------------------

@login_required(login_url='/accounts/login')
def dashboard_view(request):
    nombre_vista = 'Dashboard'
    ruta_vista = ['Dashboard']

    # Variables de reporte mensual
    cantidadPlatosMes=900
    porcentajeRespectoMesAnterior=112.5

    porcentajeComprasMesActual=18
    montoComprasMesActual=10390.50
    porcentajeVentasMesActual=17
    montoVentasMesActual=35215.48
    porcentajeIngresosMesActual=15
    montoIngresosMesActual=14568.35
    porcentajeImpuestosMesActual=14
    montoImpuestosMesActual=5482.21
    

    # Para mostrar en tabla vamos a usar GROUPBY
    # tutorial sacado de https://stackoverflow.com/a/629600/10491422
    tablaBoletasCompra = ProductoHijoCompra.objects.raw('SELECT MIN(id) AS id,MAX(id_boleta_compra) AS id_boleta_compra, MAX(id_proveedor) AS id_proveedor, SUM(precio) AS precio_total, COUNT(*) AS nro_productos FROM producto_hijo_compra GROUP BY id_boleta_compra ORDER BY id_boleta_compra DESC;')
    tablaBoletasVenta = PlatoHijoVenta.objects.raw('SELECT MIN(id) AS id, MAX(id_boleta_venta_restaurante) AS id_boleta_venta_restaurante, SUM(precio_venta) AS precio_total,  COUNT(*) AS nro_productos  FROM plato_hijo_venta GROUP BY id_boleta_venta_restaurante ORDER BY id_boleta_venta_restaurante DESC;')
    # sumaBoletasVentasMes=
    # sumaBoletasComprasMes=PlatoHijoVenta.objects.raw('SELECT MIN(id) AS id, MAX(id_boleta_venta_restaurante) AS id_boleta_venta_restaurante, SUM(precio_venta) AS precio_total,  COUNT(*) AS nro_productos  FROM plato_hijo_venta GROUP BY id_boleta_venta_restaurante ORDER BY id_boleta_venta_restaurante DESC;')
    maxItemTabla=5

    return render(request, 'dashboard.html', locals())



@login_required(login_url='/accounts/login')
def dashboard_reporte_economico_view(request):
    nombre_vista = 'Reporte económico'
    ruta_vista = ['Dashboard', 'Reporte económico']


    return render(request, 'dashboard/reporte_economico.html', locals())

# ---------------------------Fin Dashboard-------------------------


# ---------------------------------Inicio Seccion Ventas---------------------------------

# Ventas de restaurante
@login_required(login_url='/accounts/login')
def ventas_restaurante_view(request):

    #Aquí se recoje toda la información a insertar
    if request.method == 'POST':

        fecha= datetime.datetime.strptime(request.POST.get('fecha_venta'), "%d/%m/%Y")
        cantidad=request.POST.get('cantidad') #El proveedor es el mismo para todos
        importe = request.POST.get('importe')
        id_plato_padre = request.POST.get('id_plato_padre')
        id_boleta_venta_restaurante= request.POST.get('id_boleta_venta_restaurante')

        BoletaVentaRestaurante.objects.create(fecha_venta=fecha)
        
        
        # Obtener información de los productos
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

    nombre_vista = 'Ventas de Restaurante'
    ruta_vista = ['Ventas de Restaurante']
    
    productoPlato=ProductoPlato.objects.all()
    platoPadre=PlatoPadre.objects.all()
    platoHijoVenta=PlatoHijoVenta.objects.all()
    boletaVentaRestaurante=BoletaVentaRestaurante.objects.all()
    productoPadre = ProductoPadre.objects.all()
    
    # Para mostrar en tabla vamos a usar GROUPBY
    # tutorial sacado de https://stackoverflow.com/a/629600/10491422
    tablaBoletasVenta = PlatoHijoVenta.objects.raw('SELECT MIN(id) AS id, MAX(id_boleta_venta_restaurante) AS id_boleta_venta_restaurante, SUM(precio_venta) AS precio_total,  COUNT(*) AS nro_productos  FROM plato_hijo_venta GROUP BY id_boleta_venta_restaurante ORDER BY id_boleta_venta_restaurante DESC;')


    json_productoPlato = serializers.serialize("json", productoPlato)  # Usado para autocompletado
    json_platoPadre = serializers.serialize("json", platoPadre)  # Usado para autocompletado
    json_platoHijoVenta = serializers.serialize("json", platoHijoVenta)  # Usado para autocompletado
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

    tablaBoletasVenta = PlatoHijoVenta.objects.raw('SELECT MIN(id) AS id, MAX(id_boleta_venta_restaurante) AS id_boleta_venta_restaurante, SUM(precio_venta) AS precio_total,  COUNT(*) AS nro_productos  FROM plato_hijo_venta GROUP BY id_boleta_venta_restaurante ORDER BY id_boleta_venta_restaurante DESC;')

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
        id_boleta_compra = int(request.POST.get('id_boleta_compra'))
        BoletaCompra.objects.create(fecha_compra=fecha)
               
       #Si se envia el parámetro "nuevo_proveedor" significa que se debe crear un nuevo_proveedor:
        nombre_proveedor = request.POST.get('nuevo_proveedor')
        print(nombre_proveedor)
        ruc=int(request.POST.get('ruc').replace(" ",""))
        celular=int(request.POST.get('celular').replace("-",""))
        correo=request.POST.get('correo')
        
        if nombre_proveedor != None:
            Proveedor.objects.create(nombre=nombre_proveedor,ruc=ruc,celular=celular,correo=correo,fecha_creado=fecha,fecha_modificado=fecha)       
            id_proveedor=Proveedor.objects.get(nombre=nombre_proveedor).pk

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

    # Mostrar tabla boletas solo 10 ultimos
    # tutorial sacado de https://stackoverflow.com/a/629600/10491422
    tablaBoletas = ProductoHijoCompra.objects.raw('SELECT MIN(id) AS id,MAX(id_boleta_compra) AS id_boleta_compra, MAX(id_proveedor) AS id_proveedor, SUM(precio) AS precio_total, COUNT(*) AS nro_productos FROM producto_hijo_compra GROUP BY id_boleta_compra ORDER BY id_boleta_compra DESC;')

    json_proveedores = serializers.serialize("json", proveedores)  # Usado para autocompletado
    json_producto_hijo = serializers.serialize("json", productoHijoCompra)  # Usado para autocompletado
    json_producto_padre = serializers.serialize("json", productoPadre)  # Usado para autocompletado

    return render(request, 'compras_productos.html', locals())


@login_required(login_url='/accounts/login')
def compras_historial_view(request):

    nombre_vista = 'Compras Historial'
    ruta_vista = ['Compras Historial']

    tablaBoletas = ProductoHijoCompra.objects.raw('SELECT MIN(id) AS id,MAX(id_boleta_compra) AS id_boleta_compra, MAX(id_proveedor) AS id_proveedor, SUM(precio) AS precio_total, COUNT(*) AS nro_productos FROM producto_hijo_compra GROUP BY id_boleta_compra ORDER BY id_boleta_compra DESC;')

    return render(request, 'compras_historial.html', locals())


# ---------------------------------Fin Seccion Productos---------------------------------


# ---------------------------------Inicio Editar---------------------------------

@login_required(login_url='/accounts/login')
def editar_plato_view(request):

    nombre_vista = 'Editar platos'
    ruta_vista = ['Editar platos']
    
    platoHijoVenta=PlatoHijoVenta.objects.all()
    platoPadre=PlatoPadre.objects.all()
    productoPadre = ProductoPadre.objects.all()
    productoHijoCompra = ProductoHijoCompra.objects.all()
    productoPadre = ProductoPadre.objects.all()
    
    json_platoHijoVenta = serializers.serialize("json", platoHijoVenta)  # Usado para autocompletado
    json_platoPadre = serializers.serialize("json", platoPadre)  # Usado para autocompletado
    json_producto_padre = serializers.serialize("json", productoPadre)  # Usado para autocompletado
    json_producto_hijo = serializers.serialize("json", productoHijoCompra)  # Usado para autocompletado
    json_producto_padre = serializers.serialize("json", productoPadre)  # Usado para autocompletado
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
