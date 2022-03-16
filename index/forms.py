from django import forms

TYPES_OF_RECIPE = (('dulce', 'recetas dulces'),
                     ('salado', 'snacks salados'),
                     ('postres', 'postrecitos ricos'))

class BookForm(forms.Form):
  title = forms.CharField(label='Título')
  author = forms.CharField(label='Autor')
  isbn = forms.IntegerField(label='ISBN')
  
class RecipeForm(forms.Form):
  name = forms.CharField(label='Nombre')
  category = forms.MultipleChoiceField(label='Categoría',
                                       required=False,
                                       widget=forms.CheckboxSelectMultiple,
                                       choices=TYPES_OF_RECIPE)
  preparation = forms.CharField(label='Preparación', widget=forms.Textarea)
  
  
class PostForm(forms.Form):
  title = forms.CharField(label='Título')
  subtitle = forms.CharField(label='Subtítulo')
  author = forms.CharField(label='Autor')
  content = forms.CharField(label='Contenido', widget=forms.Textarea)
  published = forms.DateTimeField(label='Fecha publicación',
                                  widget=forms.DateInput,
                                  help_text='AAAA-MM-DD')
  
  
class BookSearchForm(forms.Form):
  find_book = forms.CharField(label='Título', max_length=100)
  