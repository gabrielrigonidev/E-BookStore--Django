from django.contrib import messages
from django.shortcuts import render, redirect
from appBook.form_cadastro_user import FormCadastroUser
from appBook.form_cadastro_livro import FormCadastroLivro
from appBook.models import Usuario

def appBook(request):
    return render(request, 'index.html')

def cadastrar_user(request):
    novo_user = FormCadastroUser(request.POST or None)
    if request.POST:
        if novo_user.is_valid():
            novo_user.save()
            messages.success(request, "Usuário cadastrado com sucesso!")
            return redirect('appBook')
    context = {
        'form': novo_user
    }
    return render(request, 'cadastro.html', context)

def exibir_users(request):
    usuarios = Usuario.objects.all().values()

    context = {
        'dados': usuarios
    }
    return render(request, 'usuarios.html', context)

def cadastrar_livro(request):
    novo_livro = FormCadastroLivro(request.POST or None)
    if request.POST:
        if novo_livro.is_valid():
            novo_livro.save()
            messages.success(request, "Livro adicionado com sucesso!")
            return redirect('appBook')
    context = {
        'form': novo_livro
    }
    return render(request, 'biblioteca.html', context)