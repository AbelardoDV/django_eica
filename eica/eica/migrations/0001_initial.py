# Generated by Django 3.0.1 on 2020-01-27 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
            name='BoletaCompra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.CharField(blank=True, max_length=500, null=True)),
                ('fecha_compra', models.DateTimeField(blank=True, null=True)),
                ('fecha_creado', models.DateTimeField(blank=True, null=True)),
                ('fecha_modifcado', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'boleta_compra',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='BoletaVentaRestaurante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.CharField(blank=True, max_length=500, null=True)),
                ('fecha_venta', models.DateTimeField(blank=True, null=True)),
                ('fecha_creado', models.DateTimeField(blank=True, null=True)),
                ('fecha_modificado', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'boleta_venta_restaurante',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PlatoPadre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'plato_padre',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ProductoPadre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=500, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=500, null=True)),
                ('unidad', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'producto_padre',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('ruc', models.BigIntegerField(blank=True, null=True)),
                ('correo', models.CharField(blank=True, max_length=50, null=True)),
                ('celular', models.BigIntegerField(blank=True, null=True)),
                ('fecha_creado', models.DateTimeField()),
                ('fecha_modificado', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'proveedor',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='VentaBodega',
            fields=[
                ('id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('comentario', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'venta_bodega',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ProductoPlato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.FloatField(blank=True, null=True)),
                ('id_plato_padre', models.ForeignKey(blank=True, db_column='id_plato_padre', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='eica.PlatoPadre')),
                ('id_producto_padre', models.ForeignKey(blank=True, db_column='id_producto_padre', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='eica.ProductoPadre')),
            ],
            options={
                'db_table': 'producto_plato',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ProductoHijoVenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.FloatField()),
                ('cantidad', models.FloatField(blank=True, null=True)),
                ('cliente_name', models.CharField(blank=True, max_length=50, null=True)),
                ('id_producto_padre', models.ForeignKey(blank=True, db_column='id_producto_padre', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='eica.ProductoPadre')),
                ('id_venta_bodega', models.ForeignKey(blank=True, db_column='id_venta_bodega', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='eica.VentaBodega')),
            ],
            options={
                'db_table': 'producto_hijo_venta',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ProductoHijoCompra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.FloatField()),
                ('cantidad', models.FloatField(blank=True, null=True)),
                ('id_boleta_compra', models.ForeignKey(blank=True, db_column='id_boleta_compra', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='eica.BoletaCompra')),
                ('id_producto_padre', models.ForeignKey(blank=True, db_column='id_producto_padre', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='eica.ProductoPadre')),
                ('id_proveedor', models.ForeignKey(blank=True, db_column='id_proveedor', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='eica.Proveedor')),
            ],
            options={
                'db_table': 'producto_hijo_compra',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PlatoHijoVenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio_venta', models.FloatField(blank=True, null=True)),
                ('id_boleta_venta_restaurante', models.ForeignKey(blank=True, db_column='id_boleta_venta_restaurante', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='eica.BoletaVentaRestaurante')),
                ('id_plato_padre', models.ForeignKey(blank=True, db_column='id_plato_padre', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='eica.PlatoPadre')),
            ],
            options={
                'db_table': 'plato_hijo_venta',
                'managed': True,
            },
        ),
    ]
