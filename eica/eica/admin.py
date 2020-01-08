from django.contrib import admin
from django.apps import apps

# class PersonasAdmin(admin.ModelAdmin):
#     fieldsets   =  [(None, {'fields':['nombre','edad','dni']}),('Date information', {'fields':['fecha_creado']})]
#     list_display = ('nombre','fecha_creado')
models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass