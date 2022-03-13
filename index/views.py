from turtle import title
from django.shortcuts import render
from .models import Book, Recipe, Post
from .forms import BookForm

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


