#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render_to_response,get_object_or_404
class Bebida(models.Model):
  nombre=models.CharField(max_length=50)
  ingredientes=models.TextField()
  preparacion=models.TextField()
  def __unicode__(self):
   return self.nombre
class Receta(models.Model):
  titulo=models.CharField(max_length=100, unique=True)
  ingredientes=models.TextField(help_text='Redacta los ingredientes')
  preparacion=models.TextField(verbose_name='preparacion')
  imagen=models.ImageField(upload_to='recetas', verbose_name='Imagen')
  tiempo_registro=models.DateTimeField(auto_now=True)
  usuario = models.ForeignKey(User)
  def __unicode__(self):
    return self.titulo
  