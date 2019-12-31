# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib import admin

class Personas(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    edad = models.SmallIntegerField(blank=True, null=True)
    dni = models.CharField(max_length=255, blank=True, null=True)
    fecha_creado=models.DateTimeField(auto_now=True,blank=True, null=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        managed = True
        db_table = 'personas'
        verbose_name_plural = 'personas'
