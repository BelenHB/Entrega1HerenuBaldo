from django import views
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='Home'),
    path('books/', views.books, name='Books'),
    path('recipes/', views.recipes, name='Recipes'),
    path('blog/', views.posts, name='Blog'),
    path('book-search/', views.book_search, name='Book_search'),
    path('book-author-search/', views.book_author_search, name='Book_author_search'),
]
