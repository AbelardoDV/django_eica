from django.contrib import admin
from .models import Personas

class PersonasAdmin(admin.ModelAdmin):
    fieldsets   =  [(None, {'fields':['nombre','edad','dni']}),('Date information', {'fields':['fecha_creado']})]
    list_display = ('nombre','fecha_creado')
admin.site.register(Personas,PersonasAdmin)