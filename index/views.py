from django.shortcuts import render
from .models import Book, Recipe, Post
from .forms import BookForm, RecipeForm, PostForm, BookSearchForm, BookAuthorSearchForm

# Create your views here.

# Vista HOME
def home(request):
  '''Vista de la página de inicio con mensaje de bienvenida'''
  title = 'Bienvenidos'
  subtitle = 'Esperamos que disfruten'
  content ='''Este es un espacio de encuentro para quienes disfrutamos de un 
  buen libro y algo rico para comer. ¡Súmate!'''
  return render(request, 'index/home.html', {'title':title, 'subtitle':subtitle, 
                                             'content':content})
  

# Vista LIBROS
def books(request):
  '''Permite ingresar objetos de clase Book (Libro) en la BD.
  Solicita título, autor y ISBN de la publicación'''
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
  '''Permite ingresar objetos de clase Recipe (Receta) en la BD.
  Solicita nombre, categoría (elegir entre opciones dadas) y explicación de la 
  preparación'''
  if request.method == 'POST':
    form = RecipeForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      recipe = Recipe(name=data['name'], preparation=data['preparation'])
      recipe.save()
      form = RecipeForm()
      return render(request, 'index/recipes.html', {'form':form})
  else:
    form = RecipeForm()
    
  return render(request, 'index/recipes.html',{'form':form})


# Vista BLOG
def posts(request):
  '''Permite ingresar objetos de clase Post (Publicación) en la BD.
  Solicita título, subtítulo, autor, contenido y fecha de la publicación'''
  if request.method == 'POST':
    form = PostForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      post = Post(title=data['title'], subtitle=data['subtitle'], 
                    author=data['author'], content=data['content'],
                    published=data['published'])
      post.save()
      form = PostForm()
      return render(request, 'index/posts.html', {'form':form})
  else:
    form = PostForm()
    
  return render(request, 'index/posts.html',{'form':form})


# Vista de BUSCAR LIBRO
# Para buscar libros por palabra en título
def book_search(request):
  '''Realiza una búsqueda en la BD por palabra que se encuentre en el título
  del libro'''
  books = []  #aquí se guardarán los resultados de la búsqueda
  data = request.GET.get('find_book', None)
  if data is not None:
    books = Book.objects.filter(title__icontains=data)
  searcher = BookSearchForm()
  searcher_author = BookAuthorSearchForm()
  return render(request, 'index/book_search.html',
                {'searcher':searcher, 'searcher_author':searcher_author,
                 'books':books, 'title':data})
 
 
# Para buscar libros por autor
def book_author_search(request):
  '''Realiza una búsqueda en la BD por coincidencia con autor'''
  books = []  #aquí se guardarán los resultados de la búsqueda
  data = request.GET.get('find_book_author', None)
  if data is not None:
    books = Book.objects.filter(author__icontains=data)
  searcher = BookSearchForm()
  searcher_author = BookAuthorSearchForm()
  return render(request, 'index/book_search.html',
                {'searcher':searcher, 'searcher_author':searcher_author,
                 'books':books, 'author':data})
  

  