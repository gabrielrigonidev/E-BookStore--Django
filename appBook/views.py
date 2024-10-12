from datetime import timedelta
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from appBook.models import Usuario
from appBook.forms import FormLogin, FormCadastroUser, FormCadastroLivro

def appBook(request):
    return render(request, 'index.html')

def cadastrar_user(request):
    novo_user = FormCadastroUser(request.POST or None)
    if request.POST:
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if Usuario.objects.filter(email=email).exists():
            messages.error(request, "E-mail já esta sendo utilizado!")
        elif novo_user.is_valid():
            novo_user.instance.senha = make_password(senha)
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

    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        try:
            usuario = Usuario.objects.get(email=email)
            if check_password(senha, usuario.senha):
                request.session.set_expiry(timedelta(seconds=60))
                request.session['email'] = email
                messages.success(request, "Logado com sucesso!")
                return redirect('dashboard')
            else:
                messages.error(request, "Senha incorreta.")
        except usuario.DoesNotExist:
            messages.error(request, "Usuário não encontrado.")
    context = {
        'form': formLogin
    }
    return render (request, 'form-login.html', context)

def dashboard(request):
    #Recupera a variável de Sessão
    email = request.session.get('email')

    if not request.session.get('email'):
        messages.error(request, "Você precisa estar logado para acessar o dashboard!")
        return redirect('appBook')
    context = {
            'username': email
        }
    return render(request, 'dashboard.html', context)