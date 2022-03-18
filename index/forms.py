from django import forms

# Definición de opciones para 'category' del formulario de Recetas (RecipeForm)
TYPES_OF_RECIPE = (('dulce', 'recetas dulces'),
                     ('salado', 'snacks salados'),
                     ('postres', 'postrecitos ricos'))


# Formulario para carga de libros 
class BookForm(forms.Form):
  title = forms.CharField(label='Título')
  author = forms.CharField(label='Autor')
  isbn = forms.CharField(label='ISBN', max_length=13,
                         widget=forms.NumberInput(attrs={'min':0,
                                                         'max':9999999999999}),
                         help_text='Solo números, máx. 13 caracteres')


# Formulario para carga de recetas
class RecipeForm(forms.Form):
  name = forms.CharField(label='Nombre')
  category = forms.MultipleChoiceField(label='Categoría',
                                       required=False,
                                       widget=forms.CheckboxSelectMultiple,
                                       choices=TYPES_OF_RECIPE)
  preparation = forms.CharField(label='Preparación', widget=forms.Textarea)
  
  
# Formulario de carga de publicaciones
class PostForm(forms.Form):
  title = forms.CharField(label='Título')
  subtitle = forms.CharField(label='Subtítulo')
  author = forms.CharField(label='Autor')
  content = forms.CharField(label='Contenido', widget=forms.Textarea)
  published = forms.DateTimeField(label='Fecha publicación',
                                  widget=forms.DateInput,
                                  help_text='AAAA-MM-DD')
  

# Formulario de búsqueda de libros por título
class BookSearchForm(forms.Form):
  find_book = forms.CharField(label='Título', max_length=100)


# Formulario de búsqueda de libros por autor
class BookAuthorSearchForm(forms.Form):
  find_book_author = forms.CharField(label='Autor', max_length=100)
   