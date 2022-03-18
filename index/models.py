from django.db import models
from django.utils.timezone import now

# Create your models here.

class Book(models.Model):
  title = models.CharField(max_length=100, verbose_name='Título')
  author = models.CharField(max_length=100, verbose_name='Autor')
  isbn = models.CharField(max_length=13, verbose_name='ISBN')
  
  def __str__(self):
    return self.title
  
  
class Recipe(models.Model):
  name = models.CharField(max_length=100, verbose_name='Nombre')
  preparation = models.TextField(verbose_name='Preparación', default='')
  
  def __str__(self):
    return self.name
  
class Post(models.Model):
  title = models.CharField(max_length=100, verbose_name='Título')
  subtitle = models.CharField(max_length=100, verbose_name='Subtítulo')
  author = models.CharField(max_length=100, verbose_name='Autor')
  content = models.TextField(verbose_name='Contenido')
  published = models.DateField(default=now, verbose_name='Fecha publicación')
  
  def __str__(self):
    return self.title
  
  
  