from django.contrib import admin
from .models import Book, Recipe, Post

# Register your models here.

admin.site.register(Book)

admin.site.register(Recipe)

admin.site.register(Post)
