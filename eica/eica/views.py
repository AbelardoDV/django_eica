# from django.http import HttpResponse
# from eica.models import Personas
from django.shortcuts import render
from django.contrib.auth.decorators import login_required





@login_required(login_url='/accounts/login')
def dashboard_view(request):
    nombre_vista = 'Dashboard'
    ruta_vista = ['Dashboard']
    return render(request,'dashboard.html',locals())    

@login_required(login_url='/accounts/login')
def ventas_view(request):
    nombre_vista = 'Ventas de Restaurante'
    ruta_vista = ['Ventas de Restaurante']
    return render(request,'ventas.html',locals())  
