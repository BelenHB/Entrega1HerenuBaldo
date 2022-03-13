from django import forms

class BookForm(forms.Form):
  title = forms.CharField(label='Título')
  author = forms.CharField(label='Autor')
  isbn = forms.IntegerField(label='ISBN')