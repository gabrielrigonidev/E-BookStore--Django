from django import forms
from appBook.models import Livro

class FormCadastroLivro(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ('titulo','autor','genero','paginas','preco')
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control m-2'}),
            'autor': forms.TextInput(attrs={'class':'form-control m-2'}),
            'genero': forms.TextInput(attrs={'class':'form-control m-2'}),
            'paginas': forms.NumberInput(attrs={'class': 'form-control m-2'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control m-2', 'step': '0.01'})
        }