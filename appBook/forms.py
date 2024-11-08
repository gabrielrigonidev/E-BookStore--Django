from django import forms
from appBook.models import Livro, Usuario, Foto

class FormCadastroUser(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('nome','email','senha','foto')
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control m-2', 'placeholder':'seu nome aqui'}),
            'email': forms.EmailInput(attrs={'class':'form-control m-2', 'placeholder':'usuario@email.com'}),
            'senha': forms.PasswordInput(attrs={'class':'form-control m-2'}),
            'foto': forms.FileInput(attrs={'class':'form-control m-2', 'accept':'image/*'})
        }

class FormCadastroLivro(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ('titulo','autor','genero','paginas','preco','foto')
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control m-2'}),
            'autor': forms.TextInput(attrs={'class':'form-control m-2'}),
            'genero': forms.TextInput(attrs={'class':'form-control m-2'}),
            'paginas': forms.NumberInput(attrs={'class': 'form-control m-2'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control m-2', 'step': '0.01'}),
            'foto': forms.FileInput(attrs={'class':'form-control m-2', 'accept':'image/*'})
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

class FormFoto(forms.ModelForm):
    class Meta:
        model = Foto
        fields = ['nome','foto']

        widgets = {
            'foto': forms.FileInput(attrs={'accept':'image/*'})
        }