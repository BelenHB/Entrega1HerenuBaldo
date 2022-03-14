from turtle import title
from django.shortcuts import render
from .models import Book, Recipe, Post
from .forms import BookForm, RecipeForm, PostForm

# Create your views here.

# Vista HOME
def home(request):
  title = 'Bienvenidos'
  subtitle = 'Esperamos que disfruten'
  content ='Este es un espacio de encuentro para quienes disfrutamos de un buen libro y algo rico para comer. ¡Súmate!'
  return render(request, 'index/home.html', 
                {'title':title,
                 'subtitle':subtitle,
                'content':content})
  

# Vista LIBROS
def books(request):
  if request.method == 'POST':
    form = BookForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      book = Book(title=data['title'], author=data['author'], isbn=data['isbn'])
      book.save()
      form = BookForm()
      return render(request, 'index/books.html', {'form':form})
  else:
    form = BookForm()
    
  return render(request, 'index/books.html',{'form':form})


# Vista RECETAS
def recipes(request):
  if request.method == 'POST':
    form = RecipeForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      recipe = Recipe(name=data['name'], category=data['category'], preparation=data['preparation'])
      recipe.save()
      form = RecipeForm()
      return render(request, 'index/recipes.html', {'form':form})
  else:
    form = RecipeForm()
    
  return render(request, 'index/recipes.html',{'form':form})


# Vista BLOG
def posts(request):
  if request.method == 'POST':
    form = PostForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      recipe = Post(title=data['title'], subtitle=data['subtitle'], 
                    author=data['author'], content=data['content'],
                    published=data['published'])
      recipe.save()
      form = PostForm()
      return render(request, 'index/posts.html', {'form':form})
  else:
    form = PostForm()
    
  return render(request, 'index/posts.html',{'form':form})