# Generated by Django 3.0.1 on 2019-12-30 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eica', '0002_personas_dni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personas',
            name='dni',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]