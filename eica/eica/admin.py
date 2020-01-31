from django.contrib import admin
from django.apps import apps

from eica.models import *

ban = ['django_session',
       'django_migrations',
       'django_content_type',
       'auth_user_user_permissions',
       'auth_group',
       'auth_group_permissions',
       'auth_permission',
       'auth_user',
       'auth_user_groups',
       'django_admin_log']


# ---------------- INICIO Columnas específicas en Django admin------------------

class BoletaCompraAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'comentario',
                    'valido',
                    'proveedor',
                    'fecha_compra',
                    'fecha_creado',
                    'fecha_modificado')


admin.site.register(BoletaCompra, BoletaCompraAdmin)


class BoletaVentaRestauranteAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'comentario',
                    'cliente',
                    'fecha_venta',
                    'fecha_creado',
                    'fecha_modificado')


admin.site.register(BoletaVentaRestaurante, BoletaVentaRestauranteAdmin)


class PlatoPadreAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'nombre')


admin.site.register(PlatoPadre, PlatoPadreAdmin)


class PlatoHijoVentaAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'precio_venta',
                    'cantidad',
                    'plato_padre',
                    'boleta_venta_restaurante')


admin.site.register(PlatoHijoVenta, PlatoHijoVentaAdmin)


class ProductoHijoCompraAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'precio',
                    'cantidad',
                    'boleta_compra',
                    'producto_padre')


admin.site.register(ProductoHijoCompra, ProductoHijoCompraAdmin)


class ProductoHijoVentaAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'precio',
                    'cantidad',
                    'venta_bodega',
                    'producto_padre',
                    'cliente_name')


admin.site.register(ProductoHijoVenta, ProductoHijoVentaAdmin)


class ProductoPadreAdmin(admin.ModelAdmin):
    list_display = ('nombre',
                    'descripcion',
                    'unidad')


admin.site.register(ProductoPadre, ProductoPadreAdmin)


class ProductoPlatoAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'cantidad',
                    'producto_padre',
                    'plato_padre')


admin.site.register(ProductoPlato, ProductoPlatoAdmin)


class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'nombre',
                    'ruc',
                    'correo',
                    'celular',
                    'fecha_creado',
                    'fecha_modificado')


admin.site.register(Proveedor, ProveedorAdmin)


class VentaBodegaAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'comentario')


admin.site.register(VentaBodega, VentaBodegaAdmin)


# ---------------- FIN Columnas específicas en Django admin------------------


models = apps.get_models()
for model in models:
    if model._meta.db_table not in ban:
        try:
            admin.site.register(model)
        except admin.sites.AlreadyRegistered:
            pass
