# Generated by Django 3.0.2 on 2020-01-31 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eica', '0011_auto_20200130_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='boletaventarestaurante',
            name='numero',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
