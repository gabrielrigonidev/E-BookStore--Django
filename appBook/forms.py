from django import forms
from appBook.models import Livro
from appBook.models import Usuario

class FormCadastroUser(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('nome','email','senha')
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control m-2', 'placeholder':'seu nome aqui'}),
            'email': forms.EmailInput(attrs={'class':'form-control m-2', 'placeholder':'usuario@email.com'}),
            'senha': forms.PasswordInput(attrs={'class':'form-control m-2'})
        }

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

class FormLogin(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('email', 'senha')

        widgets = {
            'email': forms.EmailInput(attrs={'class':'form-control m-2', 'placeholder':'usuario@email.com'}),
            'senha': forms.PasswordInput(attrs={'class':'form-control m-2'})
        }

class FormEditarUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('email', 'senha')

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control m-2', 'placeholder': 'usuario@email.com'}),
            'senha': forms.PasswordInput(attrs={'class': 'form-control m-2'})
        }

    def __init__(self, *args, **kwargs):
        super(FormEditarUsuario, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['readonly'] = True
