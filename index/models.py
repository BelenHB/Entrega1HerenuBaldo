from django.db import models

# Create your models here.

class Book(models.Model):
  title = models.CharField(max_length=100, verbose_name='Título')
  author = models.CharField(max_length=100, verbose_name='Autor')
  isbn = models.IntegerField()
  
  def __str__(self):
    return self.title
  
  
class Recipe(models.Model):
  name = models.CharField(max_length=100, verbose_name='Nombre')
  TYPES_OF_RECIPE = (('dulce', 'recetas dulces'),
                     ('salado', 'snacks salados'),
                     ('postres', 'postrecitos ricos'))
  category = models.CharField(max_length= 100, verbose_name='Categoría', choices=TYPES_OF_RECIPE)
  # preparation = models.TextField(verbose_name='Preparación')
  
  def __str__(self):
    return self.name
  
class Post(models.Model):
  title = models.CharField(max_length=100, verbose_name='Título')
  subtitle = models.CharField(max_length=100, verbose_name='Subtítulo')
  author = models.CharField(max_length=100, verbose_name='Autor')
  content = models.TextField(verbose_name='Contenido')
  published = models.DateTimeField(verbose_name='Fecha publicación', auto_now_add=True)
  
  def __str__(self):
    return self.title
  
  
  