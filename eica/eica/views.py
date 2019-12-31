# from django.http import HttpResponse
from django.shortcuts import render
from eica.models import Personas
from django.contrib.auth.decorators import login_required

def homepage_view(request, *args, **kwargs):
    # return HttpResponse("Home")
    return render(request,'home.html',{})

@login_required(login_url='/accounts/login')
def table_view(request):
    personas = Personas.objects.all()
    return render(request,'table.html',locals())    


def apinuevo(request):
    personas = Personas.objects.all()
    return render(request,'apinuevo.html',locals())    

