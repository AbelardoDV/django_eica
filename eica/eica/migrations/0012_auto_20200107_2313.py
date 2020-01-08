# Generated by Django 3.0.1 on 2020-01-08 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eica', '0011_clientes_compras_controlflujocaja_listaplatosporventas_listaproductosporcompras_listaproductosporpla'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BoletaCompra',
            fields=[
                ('id_boleta_compra', models.AutoField(primary_key=True, serialize=False)),
                ('comentarios_compras', models.CharField(blank=True, max_length=500, null=True)),
                ('fecha_compra', models.DateTimeField(blank=True, null=True)),
                ('fecha_creado', models.DateTimeField(blank=True, null=True)),
                ('fecha_modifcado', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'boleta_compra',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BoletaVentaRestaurante',
            fields=[
                ('id_venta_restaurante', models.AutoField(primary_key=True, serialize=False)),
                ('comentarios_venta_restaurante', models.CharField(blank=True, max_length=500, null=True)),
                ('fecha_venta', models.DateTimeField(blank=True, null=True)),
                ('fecha_creado', models.DateTimeField(blank=True, null=True)),
                ('fecha_modificado', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'boleta_venta_restaurante',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PlatoPadre',
            fields=[
                ('id_plato_padre', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_plato', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'plato_padre',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PlatoVenta',
            fields=[
                ('id_plato_venta', models.AutoField(primary_key=True, serialize=False)),
                ('precio_venta', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'plato_venta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductoHijoCompra',
            fields=[
                ('id_producto_hijo_compra', models.AutoField(primary_key=True, serialize=False)),
                ('precio_producto', models.FloatField()),
                ('cantidad_producto', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'producto_hijo_compra',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductoHijoVenta',
            fields=[
                ('id_producto_hijo_venta', models.AutoField(primary_key=True, serialize=False)),
                ('precio_producto', models.FloatField()),
                ('cantidad_producto', models.FloatField(blank=True, null=True)),
                ('cliente_name', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'producto_hijo_venta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductoPadre',
            fields=[
                ('nombre_producto', models.CharField(blank=True, max_length=500, null=True)),
                ('descripcion_producto', models.CharField(blank=True, max_length=500, null=True)),
                ('unidad_producto', models.CharField(blank=True, max_length=20, null=True)),
                ('id_producto_padre', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'producto_padre',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductoPlato',
            fields=[
                ('id_producto_plato', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad_producto', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'producto_plato',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id_proveedor', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_proveedor', models.CharField(max_length=200)),
                ('ruc_proveedor', models.BigIntegerField(blank=True, null=True)),
                ('correo_proveedor', models.CharField(blank=True, max_length=50, null=True)),
                ('celular_proveedor', models.BigIntegerField(blank=True, null=True)),
                ('fecha_creado', models.DateTimeField()),
                ('fecha_modificado', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'proveedor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VentaBodega',
            fields=[
                ('id_venta_bodega', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('comentarios_venta_bodega', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'venta_bodega',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Clientes',
        ),
        migrations.DeleteModel(
            name='ControlFlujoCaja',
        ),
        migrations.RemoveField(
            model_name='listaplatosporventas',
            name='id_venta_restaurante_ventas_restaurante',
        ),
        migrations.RemoveField(
            model_name='listaproductosporcompras',
            name='id_compra_compras',
        ),
        migrations.RemoveField(
            model_name='listaproductosporplatos',
            name='id_producto_productos',
        ),
        migrations.RemoveField(
            model_name='listaproductosporventa',
            name='id_producto_productos',
        ),
        migrations.DeleteModel(
            name='Platos',
        ),
        migrations.DeleteModel(
            name='Proveedores',
        ),
        migrations.DeleteModel(
            name='Transacciones',
        ),
        migrations.DeleteModel(
            name='Usuarios',
        ),
        migrations.DeleteModel(
            name='VentasBodega',
        ),
        migrations.DeleteModel(
            name='Compras',
        ),
        migrations.DeleteModel(
            name='ListaPlatosPorVentas',
        ),
        migrations.DeleteModel(
            name='ListaProductosPorCompras',
        ),
        migrations.DeleteModel(
            name='ListaProductosPorPlatos',
        ),
        migrations.DeleteModel(
            name='ListaProductosPorVenta',
        ),
        migrations.DeleteModel(
            name='Productos',
        ),
        migrations.DeleteModel(
            name='VentasRestaurante',
        ),
    ]
