from unicodedata import name
from django import views
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='Home'),
    path('books/', views.books, name='Books'),
    path('recipes/', views.recipes, name='Recipes'),
    path('blog/', views.posts, name='Blog'),
]
