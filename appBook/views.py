from datetime import timedelta
from django.contrib import messages
from django.shortcuts import render, redirect
from appBook.forms import FormCadastroLivro
from appBook.forms import FormCadastroUser
from appBook.forms import FormLogin
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

def form_login(request):
    formLogin = FormLogin(request.POST or None)

    if request.POST:
        _email = request.POST['email']
        _senha = request.POST['senha']
        try:
            usuario = Usuario.objects.get(email=_email, senha=_senha)
            if usuario is not None:
                request.session.set_expiry(timedelta(seconds=60))
                request.session['email'] = _email

                messages.success(request, "Logado com sucesso!")
                return redirect('dashboard')
        except:
            messages.error(request, "Deu ruim parceiro")
            return redirect('form_login')

    context = {
        'form': formLogin
    }
    return render (request, 'form-login.html', context)

def dashboard(request):
    #Recupera a variável de Sessão
    email = request.session.get('email')

    context = {
            'username': email
        }

    return render(request, 'dashboard.html', context)