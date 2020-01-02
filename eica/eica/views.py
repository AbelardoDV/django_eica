# from django.http import HttpResponse
# from eica.models import Personas
from django.shortcuts import render
from django.contrib.auth.decorators import login_required





@login_required(login_url='/accounts/login')
def dashboard_view(request):
    nombre_vista = 'Dashboard'
    ruta_vista = ['Dashboard']
    return render(request,'dashboard.html',locals())    

#---------------------------------Inicio Seccion Ventas--------------------------------- 

#Ventas de restaurante
@login_required(login_url='/accounts/login')
def ventas_restaurante_view(request):
    nombre_vista = 'Ventas de Restaurante'
    ruta_vista = ['Ventas de Restaurante']
    return render(request,'ventas_restaurante.html',locals())  

#Ventas de bodega
@login_required(login_url='/accounts/login')
def ventas_bodega_view(request):
    nombre_vista = 'Ventas de Bodega'
    ruta_vista = ['Ventas de Bodega']
    return render(request,'ventas_bodega.html',locals())  

#Historial de Ventas
@login_required(login_url='/accounts/login')
def ventas_historial_view(request):
    nombre_vista = 'Historial de Ventas'
    ruta_vista = ['Historial de Ventas']
    return render(request,'ventas_historial.html',locals())  


##---------------------------------Fin Seccion Ventas---------------------------------

#---------------------------------Inicio Seccion Productos--------------------------------- 
@login_required(login_url='/accounts/login')
def compras_productos_view(request):
    nombre_vista = 'Compras de Productos'
    ruta_vista = ['Compras de Productos']
    return render(request,'compras_productos.html',locals())  

@login_required(login_url='/accounts/login')
def compras_historial_view(request):
    nombre_vista = 'Compras Historial'
    ruta_vista = ['Compras Historial']
    return render(request,'compras_historial.html',locals())  

##---------------------------------Fin Seccion Productos---------------------------------