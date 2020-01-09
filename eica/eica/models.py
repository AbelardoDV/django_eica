# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BoletaCompra(models.Model):
    id_boleta_compra = models.AutoField(primary_key=True)
    comentarios_compras = models.CharField(
        max_length=500, blank=True, null=True)
    fecha_compra = models.DateTimeField(blank=True, null=True)
    fecha_creado = models.DateTimeField(blank=True, null=True)
    fecha_modifcado = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'boleta_compra'

    def __str__(self):
        return '{}'.format(self.id_boleta_compra)

class BoletaVentaRestaurante(models.Model):
    id_venta_restaurante = models.AutoField(primary_key=True)
    comentarios_venta_restaurante = models.CharField(
        max_length=500, blank=True, null=True)
    fecha_venta = models.DateTimeField(blank=True, null=True)
    fecha_creado = models.DateTimeField(blank=True, null=True)
    fecha_modificado = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'boleta_venta_restaurante'
        
    def __str__(self):
        return '{}'.format(self.id_venta_restaurante)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey(
        'DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
        

class PlatoPadre(models.Model):
    id_plato_padre = models.AutoField(primary_key=True)
    nombre_plato = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'plato_padre'

    def __str__(self):
        return '{}'.format(self.id_plato_padre)



class PlatoVenta(models.Model):
    id_plato_venta = models.AutoField(primary_key=True)
    precio_venta = models.FloatField(blank=True, null=True)
    id_plato_padre_plato_padre = models.ForeignKey(
        PlatoPadre, models.DO_NOTHING, db_column='id_plato_padre_plato_padre', blank=True, null=True)
    id_venta_restaurante_boleta_venta_restaurante = models.ForeignKey(
        BoletaVentaRestaurante, models.DO_NOTHING, db_column='id_venta_restaurante_boleta_venta_restaurante', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plato_venta'

    def __str__(self):
        return '{}'.format(self.id_plato_venta)

class ProductoHijoCompra(models.Model):
    id_producto_hijo_compra = models.AutoField(primary_key=True)
    precio_producto = models.FloatField()
    id_proveedor_proveedor = models.ForeignKey(
        'Proveedor', models.DO_NOTHING, db_column='id_proveedor_proveedor', blank=True, null=True)
    cantidad_producto = models.FloatField(blank=True, null=True)
    id_boleta_compra_boleta_compra = models.ForeignKey(
        BoletaCompra, models.DO_NOTHING, db_column='id_boleta_compra_boleta_compra', blank=True, null=True)
    id_producto_padre_producto_padre = models.ForeignKey(
        'ProductoPadre', models.DO_NOTHING, db_column='id_producto_padre_producto_padre', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto_hijo_compra'

    def __str__(self):
        return '{}'.format(self.id_producto_hijo_compra)

class ProductoHijoVenta(models.Model):
    id_producto_hijo_venta = models.AutoField(primary_key=True)
    precio_producto = models.FloatField()
    cantidad_producto = models.FloatField(blank=True, null=True)
    id_venta_bodega_venta_bodega = models.ForeignKey(
        'VentaBodega', models.DO_NOTHING, db_column='id_venta_bodega_venta_bodega', blank=True, null=True)
    id_producto_padre_producto_padre = models.ForeignKey(
        'ProductoPadre', models.DO_NOTHING, db_column='id_producto_padre_producto_padre', blank=True, null=True)
    cliente_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto_hijo_venta'
        
    def __str__(self):
        return '{}'.format(self.id_producto_hijo_venta)

class ProductoPadre(models.Model):
    nombre_producto = models.CharField(max_length=500, blank=True, null=True)
    descripcion_producto = models.CharField(
        max_length=500, blank=True, null=True)
    unidad_producto = models.CharField(max_length=20, blank=True, null=True)
    id_producto_padre = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'producto_padre'

    def __str__(self):
        return '{}'.format(self.id_producto_padre)


class ProductoPlato(models.Model):
    id_producto_padre_producto_padre = models.ForeignKey(
        ProductoPadre, models.DO_NOTHING, db_column='id_producto_padre_producto_padre', blank=True, null=True)
    id_producto_plato = models.AutoField(primary_key=True)
    cantidad_producto = models.FloatField(blank=True, null=True)
    id_plato_padre_plato_padre = models.ForeignKey(
        PlatoPadre, models.DO_NOTHING, db_column='id_plato_padre_plato_padre', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto_plato'

    def __str__(self):
        return '{}'.format(self.id_producto_padre_producto_padre)

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

    def __str__(self):
        return '{}'.format(self.id_proveedor)


class VentaBodega(models.Model):
    id_venta_bodega = models.SmallIntegerField(primary_key=True)
    comentarios_venta_bodega = models.CharField(
        max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'venta_bodega'

    def __str__(self):
        return '{}'.format(self.id_venta_bodega)