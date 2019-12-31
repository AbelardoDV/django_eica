# from django.http import HttpResponse
from django.shortcuts import render
# from eica.models import Personas
from django.contrib.auth.decorators import login_required

def homepage_view(request, *args, **kwargs):
    # return HttpResponse("Home")
    return render(request,'home.html',{})

@login_required(login_url='/accounts/login')
def table_view(request):
    # personas = Personas.objects.all()
    return render(request,'table.html',locals())    


@login_required(login_url='/accounts/login')
def ventas_view(request):
    # personas = Personas.objects.all()
    return render(request,'controlador/ventas.html',locals())    

# def apinuevo(request):
#     personas = Personas.objects.all()
    
#     if request.method=='POST':
#         form=PersonasForm(request.POST)
#         if form.is_valid():
#             form.save()
#         # return redirect('apinuevo:apinuevo')
#     else:
#         form=PersonasForm()
    
#     return render(request,'apinuevo.html',{'p':personas,'form':form})    

