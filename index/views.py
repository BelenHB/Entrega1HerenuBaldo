from django.shortcuts import render


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
  

