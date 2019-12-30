from django.shortcuts import render
from django.http import HttpResponse

def homepage_view(request,*args,**kwargs):
    # return HttpResponse("Home")
    print(args,kwargs)
    return render(request,"home.html",{})