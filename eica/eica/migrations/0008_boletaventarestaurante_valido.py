# Generated by Django 3.0.2 on 2020-01-30 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eica', '0007_auto_20200129_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='boletaventarestaurante',
            name='valido',
            field=models.BooleanField(default=True),
        ),
    ]