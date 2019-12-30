from django.shortcuts import render
from django.http import HttpResponse
from eica.models import *

def homepage_view(request,*args,**kwargs):
    # return HttpResponse("Home")
    personas = Personas.objects.all()
           
    return render(request,'home.html',locals())