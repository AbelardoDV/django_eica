from django.shortcuts import render
from django.http import HttpResponse

def homepage_view(*args,**kwargs):
    # return HttpResponse("Home")
    return HttpResponse("<h1>Hola abe</h1>")