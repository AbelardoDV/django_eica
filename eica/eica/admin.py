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
    list_display = ('id_boleta_compra',
                    'comentarios_compras',
                    'fecha_compra',
                    'fecha_creado',
                    'fecha_modifcado')

admin.site.register(BoletaCompra, BoletaCompraAdmin)

class BoletaVentaRestauranteAdmin(admin.ModelAdmin):
    list_display = ('id_venta_restaurante',
                    'comentarios_venta_restaurante',
                    'fecha_venta',
                    'fecha_creado',
                    'fecha_modificado')

admin.site.register(BoletaVentaRestaurante, BoletaVentaRestauranteAdmin)

class PlatoPadreAdmin(admin.ModelAdmin):
    list_display = ('id_plato_padre',
                    'nombre_plato')

admin.site.register(PlatoPadre, PlatoPadreAdmin)

class PlatoVentaAdmin(admin.ModelAdmin):
    list_display = ('id_plato_venta',
                    'precio_venta',
                    'id_plato_padre_plato_padre',
                    'id_venta_restaurante_boleta_venta_restaurante')

admin.site.register(PlatoVenta, PlatoVentaAdmin)

class ProductoHijoCompraAdmin(admin.ModelAdmin):
    list_display = ('id_producto_hijo_compra',
                    'precio_producto',
                    'id_proveedor_proveedor',
                    'cantidad_producto',
                    'id_boleta_compra_boleta_compra',
                    'id_producto_padre_producto_padre')

admin.site.register(ProductoHijoCompra, ProductoHijoCompraAdmin)

class ProductoHijoVentaAdmin(admin.ModelAdmin):
    list_display = ('id_producto_hijo_venta',
                    'precio_producto',
                    'cantidad_producto',
                    'id_venta_bodega_venta_bodega',
                    'id_producto_padre_producto_padre',
                    'cliente_name')

admin.site.register(ProductoHijoVenta, ProductoHijoVentaAdmin)

class ProductoPadreAdmin(admin.ModelAdmin):
    list_display = ('nombre_producto',
                    'descripcion_producto',
                    'unidad_producto',
                    'id_producto_padre')
    
admin.site.register(ProductoPadre, ProductoPadreAdmin)


class ProductoPlatoAdmin(admin.ModelAdmin):
    list_display = ('id_producto_padre_producto_padre',
                    'id_producto_plato',
                    'cantidad_producto',
                    'id_plato_padre_plato_padre')

admin.site.register(ProductoPlato, ProductoPlatoAdmin)

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id_proveedor',
                    'nombre_proveedor',
                    'ruc_proveedor',
                    'correo_proveedor',
                    'celular_proveedor',
                    'fecha_creado',
                    'fecha_modificado')

admin.site.register(Proveedor, ProveedorAdmin)

class VentaBodegaAdmin(admin.ModelAdmin):
    list_display = ('id_venta_bodega',
                    'comentarios_venta_bodega')

admin.site.register(VentaBodega, VentaBodegaAdmin)
# ---------------- FIN Columnas específicas en Django admin------------------




models = apps.get_models()
for model in models:
    if model._meta.db_table not in ban:
        try:
            admin.site.register(model)
        except admin.sites.AlreadyRegistered:
            pass
