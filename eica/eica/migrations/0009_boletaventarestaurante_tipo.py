# Generated by Django 3.0.2 on 2020-01-30 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eica', '0008_boletaventarestaurante_valido'),
    ]

    operations = [
        migrations.AddField(
            model_name='boletaventarestaurante',
            name='tipo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
