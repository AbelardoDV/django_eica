# from django.http import HttpResponse
# from eica.models import Personas
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def homepage_view(request, *args, **kwargs):
    # return HttpResponse("Home")
    return render(request,'home.html',{})

@login_required(login_url='/accounts/login')
def dashboard_view(request):
    return render(request,'dashboard.html',locals())    

