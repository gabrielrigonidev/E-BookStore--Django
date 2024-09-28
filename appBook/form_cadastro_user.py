from django import forms
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