# Generated by Django 3.0.1 on 2020-01-26 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eica', '0002_auto_20200126_1123'),
    ]

    operations = [
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
        )
    ]
