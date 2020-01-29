# Generated by Django 3.0.1 on 2020-01-29 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eica', '0003_boletaventarestaurante_cliente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productohijocompra',
            name='id_proveedor',
        ),
        migrations.AddField(
            model_name='boletacompra',
            name='id_proveedor',
            field=models.ForeignKey(blank=True, db_column='id_proveedor', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='eica.Proveedor'),
        ),
    ]
