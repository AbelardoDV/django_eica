# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Clientes(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    dni_cliente = models.IntegerField(blank=True, null=True)
    comentarios_cliente = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientes'


class Compras(models.Model):
    id_compra = models.AutoField(primary_key=True)
    comentarios_compras = models.CharField(max_length=500, blank=True, null=True)
    id_transacciones_transacciones = models.OneToOneField('Transacciones', models.DO_NOTHING, db_column='id_transacciones_transacciones', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compras'


class ControlFlujoCaja(models.Model):
    id_control_flujo_caja = models.AutoField(primary_key=True)
    monto_ajuste_caja = models.FloatField(blank=True, null=True)
    fecha_apertura_caja = models.DateTimeField(blank=True, null=True)
    fecha_cierre_caja = models.DateTimeField(blank=True, null=True)
    fecha_modificado_caja = models.DateTimeField(blank=True, null=True)
    id_usuario_usuarios = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='id_usuario_usuarios', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'control_flujo_caja'


class ListaPlatosPorVentas(models.Model):
    id_venta_restaurante_ventas_restaurante = models.OneToOneField('VentasRestaurante', models.DO_NOTHING, db_column='id_venta_restaurante_ventas_restaurante', primary_key=True)
    id_plato_platos = models.ForeignKey('Platos', models.DO_NOTHING, db_column='id_plato_platos')
    precio_venta_unitario = models.FloatField(blank=True, null=True)
    cantidad = models.FloatField(blank=True, null=True)
    descuento = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lista_platos_por_ventas'
        unique_together = (('id_venta_restaurante_ventas_restaurante', 'id_plato_platos'),)


class ListaProductosPorCompras(models.Model):
    id_compra_compras = models.OneToOneField(Compras, models.DO_NOTHING, db_column='id_compra_compras', primary_key=True)
    id_producto_productos = models.ForeignKey('Productos', models.DO_NOTHING, db_column='id_producto_productos')
    precio_compra_unitario = models.FloatField(blank=True, null=True)
    cantidad = models.FloatField(blank=True, null=True)
    descuento = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lista_productos_por_compras'
        unique_together = (('id_compra_compras', 'id_producto_productos'),)


class ListaProductosPorPlatos(models.Model):
    id_producto_productos = models.OneToOneField('Productos', models.DO_NOTHING, db_column='id_producto_productos', primary_key=True)
    id_plato_platos = models.ForeignKey('Platos', models.DO_NOTHING, db_column='id_plato_platos')
    cantidad_producto_por_plato = models.FloatField(blank=True, null=True)
    unidad_producto_por_plato = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lista_productos_por_platos'
        unique_together = (('id_producto_productos', 'id_plato_platos'),)


class ListaProductosPorVenta(models.Model):
    id_producto_productos = models.OneToOneField('Productos', models.DO_NOTHING, db_column='id_producto_productos', primary_key=True)
    id_venta_bodega_ventas_bodega = models.ForeignKey('VentasBodega', models.DO_NOTHING, db_column='id_venta_bodega_ventas_bodega')
    precio_venta_unitario = models.FloatField(blank=True, null=True)
    cantidad = models.FloatField(blank=True, null=True)
    descuento = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lista_productos_por_venta'
        unique_together = (('id_producto_productos', 'id_venta_bodega_ventas_bodega'),)


class Platos(models.Model):
    id_plato = models.AutoField(primary_key=True)
    nombre_plato = models.CharField(max_length=500)
    precio_venta_plato = models.FloatField()
    precio_compra_plato = models.FloatField()
    tipo_plato = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'platos'


class Productos(models.Model):
    id_producto = models.AutoField(primary_key=True)
    id_proveedor_proveedores = models.ForeignKey('Proveedores', models.DO_NOTHING, db_column='id_proveedor_proveedores', blank=True, null=True)
    codigo_barras_producto = models.BigIntegerField()
    nombre_producto = models.CharField(max_length=500)
    descripcion_producto_cp = models.CharField(max_length=500)
    cantidad_envases_producto = models.FloatField()
    cantidad_por_envase_producto = models.FloatField()
    unidad_producto = models.CharField(max_length=100)
    precio_producto = models.FloatField()

    class Meta:
        managed = False
        db_table = 'productos'


class Proveedores(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre_clave_proveedores = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'proveedores'


class Transacciones(models.Model):
    id_transacciones = models.AutoField(primary_key=True)
    tipo_flujo_transaccion = models.CharField(max_length=50, blank=True, null=True)
    monto_transaccion = models.FloatField(blank=True, null=True)
    fecha_creado = models.DateTimeField(blank=True, null=True)
    fecha_modificado = models.DateTimeField(blank=True, null=True)
    estado_transaccion = models.CharField(max_length=100, blank=True, null=True)
    id_cliente_clientes = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='id_cliente_clientes', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transacciones'


class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=200, blank=True, null=True)
    contraseña = models.CharField(max_length=200, blank=True, null=True)
    tipo_usuario = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios'


class VentasBodega(models.Model):
    id_venta_bodega = models.SmallIntegerField(primary_key=True)
    comentarios_venta_bodega = models.CharField(max_length=500, blank=True, null=True)
    id_transacciones_transacciones = models.OneToOneField(Transacciones, models.DO_NOTHING, db_column='id_transacciones_transacciones', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ventas_bodega'


class VentasRestaurante(models.Model):
    id_venta_restaurante = models.AutoField(primary_key=True)
    comentarios_venta_restaurante = models.CharField(max_length=500, blank=True, null=True)
    id_transacciones_transacciones = models.OneToOneField(Transacciones, models.DO_NOTHING, db_column='id_transacciones_transacciones', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ventas_restaurante'
