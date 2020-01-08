/home/abe/eica/django-apps/eica
['/home/abe/eica/django-apps/eica/AdminLte3']
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BoletaCompra(models.Model):
    id_boleta_compra = models.AutoField(primary_key=True)
    comentarios_compras = models.CharField(max_length=500, blank=True, null=True)
    fecha_compra = models.DateTimeField(blank=True, null=True)
    fecha_creado = models.DateTimeField(blank=True, null=True)
    fecha_modifcado = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'boleta_compra'


class BoletaVentaRestaurante(models.Model):
    id_venta_restaurante = models.AutoField(primary_key=True)
    comentarios_venta_restaurante = models.CharField(max_length=500, blank=True, null=True)
    fecha_venta = models.DateTimeField(blank=True, null=True)
    fecha_creado = models.DateTimeField(blank=True, null=True)
    fecha_modificado = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'boleta_venta_restaurante'


class PlatoPadre(models.Model):
    id_plato_padre = models.AutoField(primary_key=True)
    nombre_plato = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'plato_padre'


class PlatoVenta(models.Model):
    id_plato_venta = models.AutoField(primary_key=True)
    precio_venta = models.FloatField(blank=True, null=True)
    id_plato_padre_plato_padre = models.ForeignKey(PlatoPadre, models.DO_NOTHING, db_column='id_plato_padre_plato_padre', blank=True, null=True)
    id_venta_restaurante_boleta_venta_restaurante = models.ForeignKey(BoletaVentaRestaurante, models.DO_NOTHING, db_column='id_venta_restaurante_boleta_venta_restaurante', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plato_venta'


class ProductoHijoCompra(models.Model):
    id_producto_hijo_compra = models.AutoField()
    precio_producto = models.FloatField()
    id_proveedor_proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='id_proveedor_proveedor', blank=True, null=True)
    cantidad_producto = models.FloatField(blank=True, null=True)
    id_boleta_compra_boleta_compra = models.ForeignKey(BoletaCompra, models.DO_NOTHING, db_column='id_boleta_compra_boleta_compra', blank=True, null=True)
    id_producto_padre_producto_padre = models.ForeignKey('ProductoPadre', models.DO_NOTHING, db_column='id_producto_padre_producto_padre', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto_hijo_compra'


class ProductoHijoVenta(models.Model):
    id_producto_hijo_venta = models.AutoField(primary_key=True)
    precio_producto = models.FloatField()
    cantidad_producto = models.FloatField(blank=True, null=True)
    id_venta_bodega_venta_bodega = models.ForeignKey('VentaBodega', models.DO_NOTHING, db_column='id_venta_bodega_venta_bodega', blank=True, null=True)
    id_producto_padre_producto_padre = models.ForeignKey('ProductoPadre', models.DO_NOTHING, db_column='id_producto_padre_producto_padre', blank=True, null=True)
    cliente_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto_hijo_venta'


class ProductoPadre(models.Model):
    nombre_producto = models.CharField(max_length=500, blank=True, null=True)
    descripcion_producto = models.CharField(max_length=500, blank=True, null=True)
    unidad_producto = models.CharField(max_length=20, blank=True, null=True)
    id_producto_padre = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'producto_padre'


class ProductoPlato(models.Model):
    id_producto_padre_producto_padre = models.ForeignKey(ProductoPadre, models.DO_NOTHING, db_column='id_producto_padre_producto_padre', blank=True, null=True)
    id_producto_plato = models.AutoField(primary_key=True)
    cantidad_producto = models.FloatField(blank=True, null=True)
    id_plato_padre_plato_padre = models.ForeignKey(PlatoPadre, models.DO_NOTHING, db_column='id_plato_padre_plato_padre', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto_plato'


class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre_proveedor = models.CharField(max_length=200)
    ruc_proveedor = models.BigIntegerField(blank=True, null=True)
    correo_proveedor = models.CharField(max_length=50, blank=True, null=True)
    celular_proveedor = models.BigIntegerField(blank=True, null=True)
    fecha_creado = models.DateTimeField()
    fecha_modificado = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedor'


class VentaBodega(models.Model):
    id_venta_bodega = models.SmallIntegerField(primary_key=True)
    comentarios_venta_bodega = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'venta_bodega'
