# Generated by Django 3.0.2 on 2020-01-31 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eica', '0012_boletaventarestaurante_numero'),
    ]

    operations = [
        migrations.AddField(
            model_name='boletaventarestaurante',
            name='vendedor',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]